from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not host.isalnum() or len(host) > 63:
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}