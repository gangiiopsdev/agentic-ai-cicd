from fastapi import FastAPI
import subprocess
import shlex
import re

class CommandSanitizer:
    @staticmethod
def sanitize_command(command: str) -> str:
        return shlex.quote(command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = CommandSanitizer.sanitize_command(host)
    if re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        subprocess.run(["ping", sanitized_host], check=True)
    else:
        raise ValueError("Invalid host")
    return {"status": "completed"}