from fastapi import FastAPI
import subprocess
global ping

cmd = ['ping', host]
subprocess.call(cmd)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(cmd)