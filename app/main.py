from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid shell injection
    if host.isalnum() or '-' in host:
        args = ['ping', host]
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"status": "invalid_host"}