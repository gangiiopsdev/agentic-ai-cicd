from fastapi import FastAPI
import subprocess
globally_allowed_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in globally_allowed_hosts:
        return {"error": "Invalid host"}, 400

    # Safe implementation
    subprocess.call(["ping", host])

    return {"status": "completed"}