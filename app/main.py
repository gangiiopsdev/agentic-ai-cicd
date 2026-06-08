from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return {"status": "error", "message": "Host is not allowed"}

    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)