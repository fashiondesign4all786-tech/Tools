import os
import re
import tempfile
import threading
import time
from collections import defaultdict, deque
from pathlib import Path
from urllib.parse import urlparse

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024

MAX_DOWNLOAD_BYTES = int(os.getenv("MAX_DOWNLOAD_BYTES", str(200 * 1024 * 1024)))
RATE_LIMIT = int(os.getenv("RATE_LIMIT_PER_MINUTE", "5"))
requests_by_ip = defaultdict(deque)
rate_lock = threading.Lock()
TEMP_ROOT = Path(tempfile.gettempdir()) / "toolnest-downloads"
TEMP_ROOT.mkdir(parents=True, exist_ok=True)

ALLOWED_HOSTS = {
    "youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be",
    "youtube-nocookie.com", "www.youtube-nocookie.com"
}

def validate_url(raw):
    if not isinstance(raw, str) or len(raw) > 2048:
        raise ValueError("Enter a valid video URL.")
    parsed = urlparse(raw.strip())
    if parsed.scheme != "https" or not parsed.hostname:
        raise ValueError("Use a complete HTTPS video URL.")
    host = parsed.hostname.lower()
    if host not in ALLOWED_HOSTS:
        raise ValueError("This endpoint currently supports public YouTube URLs only.")
    if parsed.username or parsed.password:
        raise ValueError("URLs with embedded credentials are not supported.")
    return raw.strip()

def rate_check():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr or "unknown").split(",")[0].strip()
    now = time.time()
    with rate_lock:
        q = requests_by_ip[ip]
        while q and now - q[0] > 60:
            q.popleft()
        if len(q) >= RATE_LIMIT:
            return False
        q.append(now)
    return True

@app.get("/")
def home():
    return jsonify({
        "service": "ToolNest Video Downloader API",
        "status": "ok",
        "endpoints": ["/api/health", "/api/info", "/api/download"]
    })

@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.post("/api/info")
def info():
    if not rate_check():
        return jsonify({"error": "Too many requests. Please wait a minute and try again."}), 429
    try:
        url = validate_url((request.get_json(silent=True) or {}).get("url"))
        opts = {"quiet": True, "no_warnings": True, "noplaylist": True,
                "skip_download": True, "socket_timeout": 15,
                "extractor_args": {"youtube": {"player_client": ["web"]}}}
        with yt_dlp.YoutubeDL(opts) as ydl:
            data = ydl.extract_info(url, download=False)
        formats = []
        seen = set()
        for f in data.get("formats", []):
            if f.get("vcodec") in (None, "none"):
                continue
            ext = f.get("ext")
            height = f.get("height")
            if ext not in ("mp4", "webm") or not height:
                continue
            label = f"{height}p {ext.upper()}"
            if label not in seen:
                formats.append({"format_id": str(f.get("format_id")), "label": label,
                                "height": height, "ext": ext})
                seen.add(label)
        formats.sort(key=lambda x: x["height"])
        return jsonify({"title": data.get("title", "Video"),
                        "duration": data.get("duration"),
                        "thumbnail": data.get("thumbnail"),
                        "formats": formats[:12]})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception:
        return jsonify({"error": "Could not read this video. It may be private, age-restricted, unavailable, or temporarily unsupported. Only download content you own or are authorized to save."}), 422

@app.post("/api/download")
def download():
    if not rate_check():
        return jsonify({"error": "Too many requests. Please wait a minute and try again."}), 429
    job_dir = None
    try:
        body = request.get_json(silent=True) or {}
        url = validate_url(body.get("url"))
        format_id = str(body.get("format_id", ""))
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,30}", format_id):
            return jsonify({"error": "Choose a valid format from the available list first."}), 400
        job_dir = Path(tempfile.mkdtemp(prefix="tn-", dir=TEMP_ROOT))
        template = str(job_dir / "video.%(ext)s")
        opts = {
            "quiet": True, "no_warnings": True, "noplaylist": True,
            "outtmpl": template, "format": f"{format_id}+bestaudio[ext=m4a]/{format_id}",
            "merge_output_format": "mp4", "max_filesize": MAX_DOWNLOAD_BYTES,
            "socket_timeout": 20, "retries": 1, "fragment_retries": 1,
            "extractor_args": {"youtube": {"player_client": ["web"]}},
        }
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        candidates = [p for p in job_dir.iterdir() if p.is_file() and p.suffix.lower() in (".mp4", ".webm", ".mkv", ".m4a")]
        if not candidates:
            raise RuntimeError("No output file was created.")
        file_path = max(candidates, key=lambda p: p.stat().st_size)
        if file_path.stat().st_size > MAX_DOWNLOAD_BYTES:
            raise RuntimeError("The file exceeds this service's download size limit.")
        return send_file(file_path, as_attachment=True, download_name="toolnest-video" + file_path.suffix,
                         mimetype="application/octet-stream")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception:
        return jsonify({"error": "Download failed. The video may be unavailable, the selected format may no longer exist, or the file may exceed the service limit. Please try another available format."}), 422
    finally:
        # Keep the file briefly for send_file to finish, then remove it.
        if job_dir:
            threading.Timer(180, lambda p=job_dir: __import__("shutil").rmtree(p, ignore_errors=True)).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "10000")))
