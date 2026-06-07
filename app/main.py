from fastapi import FastAPI
import subprocess
cmd = ['ping', host]
subprocess.call(cmd)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    cmd = ['ping', host]
    subprocess.call(cmd)
    return {"status": "completed"}