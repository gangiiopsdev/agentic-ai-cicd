from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Safer implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    if not host.isalnum():
        raise ValueError("Invalid input")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}