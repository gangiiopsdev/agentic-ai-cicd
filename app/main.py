from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        # Validate and sanitize the host parameter
        if not host or any(char in host for char in '<>"&|*?{}[]`$\'):  # Basic blacklist of dangerous characters
            return "Invalid host"
        args = shlex.split(f"ping {host}")
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    return SafePing.ping(host)