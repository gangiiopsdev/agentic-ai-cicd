from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or host.strip() == '':
        raise ValueError('Invalid host')
    try:
        response = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": response.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}