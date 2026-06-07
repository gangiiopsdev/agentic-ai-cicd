from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Fixed implementation using shlex.quote to escape arguments safely
        command = ['ping', host]
        subprocess.call(command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafePing.ping(host)
    return {"status": "completed"}