from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        subprocess.call(['ping', '-c', '1', host])  # Limit to a single ping attempt
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    SafePing.safe_ping(host)
    return {"status": "completed"}