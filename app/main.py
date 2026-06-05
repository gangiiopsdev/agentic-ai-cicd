from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    # Implement your host safety check here
    return True

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "invalid host"}, 400
    subprocess.call(["ping", host])
    return {"status": "completed"}