from fastapi import FastAPI
import subprocess
import shlex

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
    subprocess.run(["ping", sanitized_host], check=True)
    return {"status": "completed"}