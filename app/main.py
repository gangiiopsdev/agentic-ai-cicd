from fastapi import FastAPI
import subprocess
class SafeHostValidator:
    def __init__(self):
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'

    def validate(self, host):
        return all(char in self.allowed_chars for char in host)

app = FastAPI()
validator = SafeHostValidator()

@app.get("/ping")
def ping(host: str):
    if not validator.validate(host):
        raise ValueError("Invalid hostname")
    result = subprocess.run(["ping", "-c", "1", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}