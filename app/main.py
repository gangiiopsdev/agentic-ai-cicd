from fastapi import FastAPI
import subprocess

class SafePing:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        return SafePing.ping(host)
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr}