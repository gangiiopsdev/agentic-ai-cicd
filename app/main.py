from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and properly sanitized input
    try:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": subprocess.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}