from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Basic sanitization, more comprehensive validation is recommended
    return ''.join(c for c in input_string if c.isalnum() or c in ['-', '.', '_', ' ', ':', '@', '#'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    subprocess.call(f'ping {safe_host}', shell=True)
    return {"status": "completed"}