from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if host.startswith('127.0.0.1') or host.startswith('localhost'):
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": str(e)}
    else:
        return {"status": "error", "message": "Invalid host"}