from fastapi import FastAPI
import subprocess
def safe_getinput(command):
    # Sanitize and validate input before using it with subprocess
    if not all(c.isalnum() for c in command) or len(command) > 100:
        raise ValueError("Invalid command")
    return subprocess.run(command.split(), capture_output=True, text=True).stdout

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isalnum() or len(host) > 100:
        return {"error": "Invalid input"}
    result = safe_getinput(f'ping -c 4 {host}')
    return {"status": "completed", "result": result}