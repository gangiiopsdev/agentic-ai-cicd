from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host in ['127.0.0.1', '::1']:  # Allow only localhost for safety
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}
    return {"status": "completed"}