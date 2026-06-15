from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return False
    return True

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}