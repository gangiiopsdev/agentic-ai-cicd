from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Define allowed hosts or use a whitelist
        if host not in ['example.com', 'localhost']:
            raise ValueError("Invalid host")
        subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafePing.safe_ping(host)
    return {"status": "completed"}