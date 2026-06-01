from fastapi import FastAPI
import subprocess

def sanitize_input(input_string):
    # Basic sanitization function
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:/-')
    return ''.join(char for char in input_string if char in allowed_chars)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safer implementation using subprocess.run with args parameter and validate arguments
    if not all(char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for char in sanitized_host) or '..' in sanitized_host:
        return {"status": "error", "message": "Invalid host input"}
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}