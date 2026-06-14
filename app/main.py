from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def call(command: str):
        subprocess.call(command.split(), shell=False)

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafeSubprocess.call(f"ping {host}")
    return {"status": "completed"}