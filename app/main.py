from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host.isalnum() and '.' in host

def sanitize_input(input_str):
    # Add more sophisticated input sanitization here if needed
    return ''.join(c for c in input_str if c.isalnum() or c.isdigit())

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not is_valid_host(sanitized_host):
        return {"status": "error", "output": "Invalid host"}
    # Secure implementation using subprocess.run with shell=False
    result = subprocess.run(["ping", sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}