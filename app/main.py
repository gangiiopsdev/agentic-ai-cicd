from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return "Host not allowed"
    return subprocess.call(f'ping {host}', shell=False)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, int) and result == 0:
        return {"status": "completed"}
    else:
        return {"status": "failed", "message": result}