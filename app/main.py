from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Simple sanitization to prevent basic injection
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Sanitized implementation
    sanitized_host = sanitize_input(host)
    subprocess.call(f'ping {sanitized_host}', shell=True)

    return {"status": "completed"}