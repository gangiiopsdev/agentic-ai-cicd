from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use socket to validate the IP address format instead of shell execution
        socket.inet_aton(host)
        subprocess.call(["ping", host])
        return {"status": "completed"}
    except socket.error:
        return {"status": "invalid host", "host": host}