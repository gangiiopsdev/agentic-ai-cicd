from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Enhanced check for local addresses and use of shell=False to prevent injection
    if host in ['localhost', '127.0.0.1']:
        args = ['ping', '-c', '4', host]
        subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed"}