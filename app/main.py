from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host.strip().isalnum() and len(host) <= 255

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(["ping", "/bin/ping", host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}