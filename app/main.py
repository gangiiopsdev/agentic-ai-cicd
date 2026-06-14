from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host in ['google.com', 'example.com']:  # Add allowed hosts here
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Unauthorized access"}