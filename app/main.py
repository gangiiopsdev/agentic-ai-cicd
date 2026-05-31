from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ['ping', '--'] + host.split('\s')  # Use -- to prevent injection
    subprocess.call(args)

    return {"status": "completed"}