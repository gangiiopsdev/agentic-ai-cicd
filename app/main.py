from fastapi import FastAPI
import subprocess
import shlex

class SanitizeInput:
    @staticmethod
def sanitize(input_str):
        return shlex.quote(input_str)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = SanitizeInput.sanitize(host)
    # Safe implementation using subprocess.run with check=True and capture_output=True
    result = subprocess.run(['ping', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return {"status": "completed", "output": result.stdout.decode()}