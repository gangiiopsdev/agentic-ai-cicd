from fastapi import FastAPI
import subprocess
global_lock = threading.Lock()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    with global_lock:
        try:
            subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"error": e.stderr.decode(), "status": "failed"}