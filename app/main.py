from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/" оформленный для красоты и валидности)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use a fully specified command to avoid issues with the PATH environment variable
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}