from fastapi import FastAPI
import subprocess
def ping(host: str):
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}