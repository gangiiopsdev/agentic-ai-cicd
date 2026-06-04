from fastapi import FastAPI
import subprocess
global_ping = ['ping', '127.0.0.1'] # Default to ping localhost for example

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_ping[1] = host # Update the target of the ping command safely
    subprocess.call(global_ping)
    return {"status": "completed"}