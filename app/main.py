from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isnumeric() and len(host) <= 3:
        # Safe ping implementation using list arguments and shell=False
        subprocess.run(['ping', '-c', '1', host], check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}