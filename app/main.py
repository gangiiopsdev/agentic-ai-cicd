from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Basic sanitization of input
    return ''.join(e for e in input_string if e.isalnum() or e in '._-')

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}