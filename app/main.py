from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    # Simple input sanitization (expand this for more robust validation)
    return ''.join(c for c in user_input if c.isalnum() or c in ['-', '.', '_', ':', '@'])

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize user input before using it with subprocess.run
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }