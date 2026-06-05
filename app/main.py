from fastapi import FastAPI
import subprocess
ALLOWED_HOSTS = ['example.com']

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in ALLOWED_HOSTS:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Unauthorized access attempted"}