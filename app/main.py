from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    return host.isalnum()

app = FastAPI()

@app.get('/home')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}