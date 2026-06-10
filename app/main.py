from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to ensure it only contains allowed characters
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        raise ValueError("Invalid host parameter")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}