from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    if not input_string.strip().isdigit():
        raise ValueError("Invalid input")
    return input_string

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}