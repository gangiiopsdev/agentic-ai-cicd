from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value):
    # Basic sanitization example: strip non-alphanumeric characters
    return ''.join(c for c in value if c.isalnum())

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize user input before using it in subprocess call
    sanitized_host = sanitize_input(host)
    subprocess.call(["ping", sanitized_host])

    return {"status": "completed"}