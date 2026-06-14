from fastapi import FastAPI
import subprocess
import shlex
import re
def sanitize_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char.isspace())

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        sanitized_host = sanitize_input(host)
        # Use a whitelist for allowed hosts instead of relying on input sanitization
        allowed_hosts = ['example.com', 'test.example.com']
        if host in allowed_hosts:
            command = ["ping", *shlex.split(sanitized_host)]
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed"}
        else:
            raise HTTPException(status_code=400, detail="Invalid host")
    else:
        raise HTTPException(status_code=400, detail="Invalid host")