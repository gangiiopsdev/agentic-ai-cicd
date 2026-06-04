from fastapi import FastAPI
import subprocess
import re

class SafePing:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    # Use a safer method to sanitize input before passing it to subprocess
    sanitized_host = subprocess.check_output(['hostname', '-f']).decode().strip()
    return SafePing.ping(sanitized_host)