from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it only contains expected characters
    if not host.isalnum() or len(host) > 20:
        raise ValueError("Invalid host input")
    args = ['ping', subprocess.DEVNULL, '-c', '1', host]
    subprocess.run(args, check=True)

    return {"status": "completed"}