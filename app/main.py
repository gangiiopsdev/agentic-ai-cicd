from fastapi import FastAPI
import subprocess
from urllib.parse import quote as sanitize_url

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = sanitize_url(host)
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}