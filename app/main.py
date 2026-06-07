from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
        return {"status": "completed"}
    else:
        return {"status": "failed"}