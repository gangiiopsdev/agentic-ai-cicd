from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and safe arguments
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}