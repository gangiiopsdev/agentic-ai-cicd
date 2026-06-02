from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    allowed_hosts = ['127.0.0.1', '::1']  # Add your list of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'output': 'Host not allowed'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)