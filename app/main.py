from fastapi import FastAPI
import subprocess
import shlex

class CommandSanitizer:
    @staticmethod
def sanitize(command: str) -> str:
        return shlex.quote(command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = CommandSanitizer.sanitize(host)
    args = ['ping', sanitized_host]
    subprocess.call(args)

    return {"status": "completed"}