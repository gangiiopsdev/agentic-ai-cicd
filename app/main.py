from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        # Use shlex.quote to sanitize the input
        safe_host = shlex.quote(host)
        subprocess.run(['ping', safe_host], check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(shlex.quote(host))

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}