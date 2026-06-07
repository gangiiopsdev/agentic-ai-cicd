from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation without shell=True
    args = ['ping', host]
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}