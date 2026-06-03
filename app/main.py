from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Secure implementation
    safe_host = subprocess.list2cmdline([host])
    if safe_host and not any(char in safe_host for char in [';', '&', '|', '(', ')']):
        subprocess.call(['ping', safe_host])
    return {'status': 'completed'}

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)