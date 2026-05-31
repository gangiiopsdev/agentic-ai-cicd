from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return {"status": "failed", "error": result.stderr}
    return {"status": "completed"}