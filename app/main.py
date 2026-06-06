from fastapi import FastAPI
import subprocess
class CommandSanitizer:
    @staticmethod
def sanitize(command: str) -> str:
        return 'ping' + command.split(' ping ')[1]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = CommandSanitizer.sanitize(host)
    subprocess.call(sanitized_host, shell=True)
    return {"status": "completed"}