from fastapi import FastAPI
import subprocess
global ping_result

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        global ping_result
        ping_result = {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        ping_result = {"status": "failed", "error": e.stderr}
    return ping_result