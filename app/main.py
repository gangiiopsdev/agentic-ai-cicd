from fastapi import FastAPI
import subprocess
class CommandSanitizer:
    @staticmethod
def sanitize(command: str) -> str:
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.'
        return ''.join(c for c in command if c in allowed_chars)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = CommandSanitizer.sanitize(host)
    subprocess.call(f'ping {sanitized_host}')
    return {"status": "completed"}