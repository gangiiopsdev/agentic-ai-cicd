from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.post("/ping")
def ping(ping_request: PingRequest):
    # Secure implementation
    subprocess.call(["ping", ping_request.host], shell=False)
    return {"status": "completed"}