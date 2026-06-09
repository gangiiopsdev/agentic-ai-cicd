from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Simple sanitization example: allow only alphanumeric characters and hyphens
    return ''.join(char for char in input_string if char.isalnum() or char == '-')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}")
    return {"status": "completed"}