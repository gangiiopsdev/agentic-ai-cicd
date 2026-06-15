from fastapi import FastAPI
import subprocess
global_host = 'localhost'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call(f'ping {global_host}', shell=True)

    return {"status": "completed"}