from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use socket to validate the host, not subprocess
        socket.gethostbyname(host)
        # Ping command without shell=True for security
        result = subprocess.call(["ping", "-c", "1", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {"status": "completed", "result": result}
    except socket.gaierror:
        return {"status": "failed", "message": "Invalid hostname"}