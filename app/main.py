from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run and avoiding shell=True
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        raise ValueError(f'Ping failed: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}