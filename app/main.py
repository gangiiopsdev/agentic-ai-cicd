from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.Popen without shell=True
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}