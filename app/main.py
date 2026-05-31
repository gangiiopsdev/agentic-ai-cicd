from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation
    if not host.isdigit() or len(host) > 15:
        return {"error": "Invalid host"}, 400
    subprocess.call(["ping", f'"{host}"'])
    return {"status": "completed"}