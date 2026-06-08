from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Basic sanitization: remove non-alphanumeric characters
    return ''.join(e for e in input_string if e.isalnum())

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}