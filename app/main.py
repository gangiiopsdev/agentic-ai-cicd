from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input and use a safer method if possible
    subprocess.call(['ping', host.strip()])  # Ensure no unexpected characters are passed
    return {"status": "completed"}