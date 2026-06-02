from fastapi import FastAPI
import subprocess
cmd = ['ping', host]
subprocess.run(cmd, check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.run(cmd, check=True, capture_output=True)
    return {"status": "completed"}