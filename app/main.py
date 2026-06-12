from fastapi import FastAPI
import os
import socket

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host to ensure it's a valid IP address or hostname
        socket.inet_pton(socket.AF_INET, host)
    except (socket.error, ValueError):
        return {"status": "failed", "error": "Invalid IP address"}

    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}