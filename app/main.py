from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Add input sanitization logic here (e.g., whitelisting allowed characters)
    return ''.join(char for char in input_string if char.isalnum() or char.isspace())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.call(args)

    return {"status": "completed"}