from fastapi import FastAPI
import subprocess
import re
class CommandValidator:
    def __init__(self):
        self.allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')

    def validate(self, command: str) -> bool:
        return all(char in self.allowed_chars for char in command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validator = CommandValidator()
    if not validator.validate(host):
        raise ValueError("Invalid hostname")
    result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {"status": "completed", "output": result.stdout}