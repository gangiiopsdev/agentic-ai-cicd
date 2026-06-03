from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.Popen with shell=False and args parameter
    subprocess.Popen(['ping', host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    ping(host)
    return {"status": "completed"}