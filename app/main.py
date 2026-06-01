from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent code injection
    args = ['ping', host.replace(';', '')]  # Example of basic sanitization
    subprocess.call(args)
    return {"status": "completed"}