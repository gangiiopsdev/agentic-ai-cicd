from fastapi import FastAPI
import subprocess
cimport socketio

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host to ensure it's a valid IP or hostname
        socket.inet_pton(socket.AF_INET, host)
        subprocess.call(["ping", host])
    except socket.error:
        return {"error": "Invalid host"}

    return {"status": "completed"}