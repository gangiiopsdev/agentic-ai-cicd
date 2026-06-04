from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}
    return {"status": "completed"}