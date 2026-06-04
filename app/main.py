from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['.', '-', '_'])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
    return {"status": "completed"}