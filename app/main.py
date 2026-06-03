from fastapi import FastAPI
import shlex
global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using a safer library for network operations
    import socket
    try:
        response = socket.gethostbyname(host)
        return {"status": "completed", "response": response}
    except socket.gaierror:
        return {"status": "failed", "message": "Host could not be resolved"}