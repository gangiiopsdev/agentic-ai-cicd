from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use a list instead of a string for shell commands to avoid injection risks
    subprocess.call(['ping', host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Call the safe function to execute the ping command safely
    safe_ping(host)
    return {"status": "completed"}