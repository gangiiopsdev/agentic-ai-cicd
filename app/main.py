from fastapi import FastAPI
import subprocess
global_args = ['ping', 'localhost']
app = FastAPI()

@app.get("/"遏)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    subprocess.call(global_args + [host])

    return {"status": "completed"}