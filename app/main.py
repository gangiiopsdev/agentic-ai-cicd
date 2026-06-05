from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Unauthorized host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}