from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        args = ['ping', host]
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"status": "invalid host"}