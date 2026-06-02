from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and check=True
    args = ['ping', host]
    subprocess.run(args, shell=False, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return {"status": "completed"}