from fastapi import FastAPI
import subprocess
global_args = ['ping', '-c', '4']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.run(global_args + [host], check=True, shell=False)

    return {"status": "completed"}