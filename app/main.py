from fastapi import FastAPI
import re
import subprocess

class HostValidator:
    def __init__(self, regex_pattern):
        self.regex = re.compile(regex_pattern)

    def validate(self, host):
        if not self.regex.match(host):
            raise ValueError("Invalid hostname")

app = FastAPI()
validator = HostValidator(r'^[a-zA-Z0-9.-]+$')

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validator.validate(host)
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}