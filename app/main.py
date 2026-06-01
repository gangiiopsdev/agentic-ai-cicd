from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation
    if not host.isalnum() and '-' in host:
        raise ValueError("Invalid input for host parameter")

    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)

    return {"status": "completed"}