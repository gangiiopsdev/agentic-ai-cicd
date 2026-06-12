from fastapi import FastAPI
import subprocess
global subprocess_path
subprocess_path = 'ping'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = [subprocess_path, host]
    subprocess.run(args)
    return {"status": "completed"}