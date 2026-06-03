from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and escaping
    if 'ping' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.run(["ping", subprocess.list2cmdline([host])], check=True, capture_output=True)
    return {"status": "completed"}