from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Safe implementation using subprocess.run with shlex.split and shell=False
    subprocess.run(['ping', host], check=True, shell=False)

class InputValidator:
    def __init__(self):
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'

    def validate(self, host):
        return all(c in self.allowed_chars for c in host)

app = FastAPI()
validator = InputValidator()

@app.get("/ping")
def ping(host: str):
    if not validator.validate(host):  # Basic validation to prevent shell injection
        return {"status": "Invalid input"}
    safe_ping(shlex.quote(host))
    return {"status": "completed"}