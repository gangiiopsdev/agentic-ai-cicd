from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(input_str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', input_str):
        raise ValueError("Invalid input")
    return input_str

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}