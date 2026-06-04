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
    global ping_lock
    with ping_lock:
        try:
            result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return {"status": "completed", "output": result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "error": str(e)}