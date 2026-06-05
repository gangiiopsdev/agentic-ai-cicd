from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def safe_ping(host: str) -> dict:
        args = ['ping', host]
        safe_args = [shlex.quote(arg) for arg in args]
        subprocess.call(safe_args)
        return {"status": "completed"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)