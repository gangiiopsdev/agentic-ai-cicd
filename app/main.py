from fastapi import FastAPI
import subprocess
global completed = False

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True)
    global completed = True
    return {"status": "completed"}