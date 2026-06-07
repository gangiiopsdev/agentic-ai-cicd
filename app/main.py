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
    # Use subprocess.run instead of subprocess.call and avoid shell=True
    result = subprocess.run([sanitized_host], capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}