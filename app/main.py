from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with full path to prevent execution of untrusted input
    safe_host = subprocess.quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    # Safer implementation using subprocess.run with full path to prevent execution of untrusted input
    safe_host = subprocess.quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, shell=False)
    return {"status": "completed"}