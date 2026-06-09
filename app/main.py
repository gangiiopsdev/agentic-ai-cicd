from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, check=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent command injection
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    SafeSubprocess.run(f"ping {host}")
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex match against allowed host patterns
    allowed_hosts = ["example.com", "test.example.com"]
    return host in allowed_hosts