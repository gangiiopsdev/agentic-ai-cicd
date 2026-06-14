from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.strip().replace('.', '').isdigit():
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        status = safe_ping(host)
        return {"status": status}
    except ValueError as e:
        return {"error": str(e)}, 400