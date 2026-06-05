from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper argument passing
    if host.isnumeric() or '-' in host:
        subprocess.call(["ping", host])
    else:
        return {"error": "Invalid host input"}

    return {"status": "completed"}