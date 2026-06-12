from fastapi import FastAPI
import subprocess

app = FastAPI()

def _safe_ping(host):
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return True
    except subprocess.CalledProcessError:
        return False

@app.get("/ping")
def ping(host: str):
    if not _safe_ping(host.replace(' ', '')):
        return {'status': 'failed', 'error': 'Invalid input'}
    output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
    return {'status': 'completed', 'output': output.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}