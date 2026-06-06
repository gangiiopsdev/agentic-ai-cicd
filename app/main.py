from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value):
    return value.replace(';', '').replace('&', '')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run without shell=True
    subprocess.run(["ping", sanitized_host], check=True)
    return {"status": "completed"}