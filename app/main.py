from fastapi import FastAPI
import subprocess
from urllib.parse import quote

app = FastAPI()

def safe_ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in '.-_')
    subprocess.call(['ping', quote(sanitized_host)])

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}