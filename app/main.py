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
        # Validate input to ensure it's a valid hostname/IP
        socket.gethostbyname(host)
    except socket.gaierror:
        return {"status": "invalid host"}

    # Safe implementation using subprocess with list of arguments
    subprocess.call(['ping', host])
    return {"status": "completed"}