from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Add input validation and sanitization logic here
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run with shell=False and explicit path
    subprocess.run(['/usr/bin/ping', sanitized_host], check=True, capture_output=True)
    return {"status": "completed"}