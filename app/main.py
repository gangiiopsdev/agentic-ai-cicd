from fastapi import FastAPI
import shlex

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
    # Ensure the host input is sanitized to prevent shell injection
    safe_host = shlex.quote(host)
    return ShellCommand.safe_ping(safe_host)