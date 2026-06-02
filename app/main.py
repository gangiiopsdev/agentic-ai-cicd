from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        socket.gethostbyname(host)
        subprocess.call(['ping', '-c', '1', host])  # Limiting the number of pings to mitigate risks
    except socket.gaierror:
        return {"status": "failed", "reason": "Invalid hostname"}
    return {"status": "completed"}