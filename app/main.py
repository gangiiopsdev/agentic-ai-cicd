from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and explicit path to executable
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and explicit path to executable
    subprocess.run(['ping', host], check=True, shell=False)
    return {"status": "completed"}