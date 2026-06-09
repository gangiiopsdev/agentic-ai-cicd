from fastapi import FastAPI
import subprocess
global allowed_hosts = ['127.0.0.1', '::1']
app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        raise ValueError(f'Host {host} is not allowed')

    # Secure implementation
    subprocess.run(['ping', host], capture_output=True, check=True)

    return {"status": "completed"}