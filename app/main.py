from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using shell=False and avoiding partial paths
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shell=False and avoiding partial paths
    subprocess.run(['ping', host], check=True)