from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def sanitize_input(host):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        return ''.join(c for c in host if c in allowed_chars)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = PingCommand.sanitize_input(host)
    subprocess.call(f'ping {sanitized_host}')
    return {"status": "completed"}