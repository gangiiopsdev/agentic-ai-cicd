from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize the host parameter to prevent command injection
    if not isinstance(host, str) or '&&' in host or ';' in host:
        raise ValueError('Invalid host input')
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}