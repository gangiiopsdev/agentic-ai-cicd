from fastapi import FastAPI
import subprocess
global_ping = 'ping -c 1' # Define the ping command without user input

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    subprocess.call([global_ping, host])
    return {"status": "completed"}