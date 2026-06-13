from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and proper argument passing
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        ping_result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": ping_result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}