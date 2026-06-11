from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in input_str if char in allowed_chars)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output([quote('ping'), quote(sanitized_host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}  # Return output if needed
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}