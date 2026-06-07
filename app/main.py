from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}