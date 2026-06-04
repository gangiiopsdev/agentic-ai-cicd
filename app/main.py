from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.strip() not in ['127.0.0.1', '::1']:
        raise ValueError('Invalid host')
    return subprocess.call(['ping', host], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

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
        return {"error": str(e)}