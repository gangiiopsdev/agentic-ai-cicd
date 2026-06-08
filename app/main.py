from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Using subprocess.run with shell=False and args tuple to avoid shell injection
    subprocess.run(['ping', host], check=True)

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
        return {"error": f"Ping failed with error: {e}"}