from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Simple sanitization: allow only alphanumeric characters and hyphens
    return ''.join(c for c in input_string if c.isalnum() or c == '-').strip()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}")
    return {"status": "completed"}