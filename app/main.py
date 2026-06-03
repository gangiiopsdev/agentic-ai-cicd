from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using a whitelist of allowed hosts
    if host in ['example.com', 'another-example.com']:
        subprocess.call(['ping', host])

    return {"status": "completed"}