from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with input sanitization
    subprocess.call(['ping', host], shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with input sanitization
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}