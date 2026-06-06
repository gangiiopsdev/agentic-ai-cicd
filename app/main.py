from fastapi import FastAPI
import subprocess
global_host = '127.0.0.1'  # Replace with a fixed, safe host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(f'ping {global_host}', shell=False)
    return {"status": "completed"}