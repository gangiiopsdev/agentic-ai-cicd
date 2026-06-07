from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if host == 'example.com':  # Example validation logic
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"status": "invalid host"}