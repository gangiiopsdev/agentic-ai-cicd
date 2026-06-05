from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.strip() not in ['127.0.0.1', '::1']:
        raise ValueError('Invalid host')
    return subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": result.stdout.decode()}
    except ValueError as e:
        return {"error": str(e)}