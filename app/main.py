from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.Popen with args instead of shell=True
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}