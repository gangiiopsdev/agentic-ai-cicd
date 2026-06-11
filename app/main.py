from fastapi import FastAPI
import subprocess
global allowed_hosts = ['localhost', '127.0.0.1']
def is_safe_host(host):
    return host in allowed_hosts
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unauthorized host')
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", 'error': e.stderr}