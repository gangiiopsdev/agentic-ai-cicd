from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Fixed implementation
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping_fixed(host: str):
    # Fixed implementation
    subprocess.call(['ping', host])