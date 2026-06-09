from fastapi import FastAPI
import subprocess
global ping

@app.get("/ping")
def ping(host: str):
    cmd = ['ping', host]
    subprocess.run(cmd, check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}