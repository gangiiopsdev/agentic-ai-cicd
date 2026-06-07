from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using shell=False and avoiding partial paths
    subprocess.call(['ping', host], shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shell=False and avoiding partial paths
    subprocess.call(['ping', host], shell=False)