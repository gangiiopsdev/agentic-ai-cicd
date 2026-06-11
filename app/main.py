from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Basic sanitization example: allow only alphanumeric and some special characters
    return ''.join(c for c in input_str if c.isalnum() or c in ['-', '.', '_', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', ']', '{', '}', ';', ':', '<', '>', ',', '/', '?', '|', '\'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}