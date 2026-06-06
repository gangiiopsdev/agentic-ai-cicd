from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host name')
    args = ['ping', '-c', '1', subprocess.check_output(['echo', host], text=True).strip()]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host name')
    return safe_ping(host)