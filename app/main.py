from fastapi import FastAPI
import subprocess
from urllib.parse import quote as sanitize_url
def ping(host: str):
    # Sanitize and validate input to prevent command injection
    if not host.isdigit():
        return {"status": "failed", "error": "Invalid input"}
    sanitized_host = sanitize_url(host)
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}