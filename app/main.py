from fastapi import FastAPI
import subprocess
global ping_lock
ping_lock = threading.Lock()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation using subprocess.run with shell=False and proper argument handling
    with ping_lock:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return {"status": "completed", "output": result.stdout.decode('utf-8')}
        else:
            return {"status": "failed", "error": result.stderr.decode('utf-8')}