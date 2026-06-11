from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Safe implementation using subprocess.Popen with shell=False and full command list
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}