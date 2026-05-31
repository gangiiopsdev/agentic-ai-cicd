from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE
globally_safe_hosts = ['127.0.0.1', '::1']  # List of safe hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_safe_hosts:
        try:
            result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.stderr}
    else:
        return {"status": "error", "message": "Unauthorized host"}