from fastapi import FastAPI
import subprocess
gl
app = FastAPI()

def ping(host: str):
    # Safe implementation using list instead of string for the command
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using list instead of string for the command
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}