from fastapi import FastAPI
import subprocess
gateway = '127.0.0.1'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}