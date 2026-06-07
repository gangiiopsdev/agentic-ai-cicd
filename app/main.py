from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    subprocess.run(command, check=True)

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/secure-ping")
def secure_ping(host: str):
    # Secure implementation
    command = ['ping', host]
    subprocess.run(command, check=True)