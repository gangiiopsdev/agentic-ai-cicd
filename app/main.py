from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in [',', '.', ' ', '-'])

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Sanitize input to prevent command injection
    sanitized_host = sanitize_input(host)

    # Use subprocess without shell=True for safer execution
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)

    return {"status": "completed", "result": result.stdout}