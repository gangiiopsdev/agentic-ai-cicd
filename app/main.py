from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = subprocess.list2cmdline(host.split())
        subprocess.run(['ping', safe_host], check=True)
app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping_endpoint(host: str):
    SafePing.ping(host)
    return {"status": "completed"}