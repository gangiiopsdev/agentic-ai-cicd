from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Basic sanitization example: allow only alphanumeric characters and a few special characters
    return ''.join(c for c in input_string if c.isalnum() or c in '.-_')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize user input
    host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}