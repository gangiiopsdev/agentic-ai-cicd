from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['127.0.0.1', '::1']  # List of safe hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_safe_hosts:
        subprocess.call(f'ping {host}', shell=False)
    else:
        return {'status': 'error', 'message': 'Unauthorized host'}

    return {'status': 'completed'}