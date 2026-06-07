from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input to prevent injection attacks
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise ValueError("Invalid host input")
    subprocess.run(['ping', '--', sanitized_host], check=True)
    return {"status": "completed"}