from fastapi import FastAPI
import subprocess
global _ping
_ping = lambda host: subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    _ping(host)
    return {"status": "completed"}