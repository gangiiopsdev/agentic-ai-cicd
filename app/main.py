from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host])

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping_safe(host: str):
    # Safe implementation
    subprocess.call(['ping', host])