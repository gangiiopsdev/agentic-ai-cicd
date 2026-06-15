from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Safe implementation using list for arguments and shell=False
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        raise ValueError(f'Failed to ping {host}: {e}')

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
        return {"status": "error", "message": str(e)}