from fastapi import FastAPI
import subprocess
class ShellCommand:
    @staticmethod
def safe_ping(host: str):
        return f'ping {host}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):