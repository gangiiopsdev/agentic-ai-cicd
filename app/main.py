from fastapi import FastAPI
import subprocess

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'
    return ''.join(char for char in input_str if char in allowed_chars)

def validate_host(host):
    # Add validation logic here, e.g., whitelist of allowed hosts
    return host.strip() == 'localhost'  # Example validation

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    host = validate_host(sanitize_input(host))
    if not host:
        return {"status": "error", "message": "Invalid host"}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}