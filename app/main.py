from fastapi import FastAPI
import subprocess
global_process = None

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global global_process
    if global_process is not None and global_process.poll() is None:
        global_process.terminate()

    global_process = subprocess.Popen(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return {"status": "completed"}