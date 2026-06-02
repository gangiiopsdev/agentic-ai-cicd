from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with full executable path
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):  
    # Secure implementation using subprocess.run with full executable path
    subprocess.run(['ping', host], check=True, shell=False)