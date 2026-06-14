from fastapi import FastAPI
import subprocess
global host
app = FastAPI()
@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not all(c.isalnum() or c in ["-"] for c in host):
        return {"error": "Invalid hostname"}
    try:
        subprocess.run(["ping", host], check=True, timeout=10)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}