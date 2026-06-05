from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.startswith('.') and ':' not in host:
        subprocess.call(['ping', host])
    else:
        raise ValueError("Invalid host")

@app.get="/ping"
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}