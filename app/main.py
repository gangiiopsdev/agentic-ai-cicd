from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    return ''.join(e for e in host if e.isalnum() or e in ['.', '-', '_'])

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.run(['ping', sanitized_host], check=True, shell=False, capture_output=True)
    return {"status": "completed"}