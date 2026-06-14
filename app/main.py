from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Basic sanitization: ensure no null bytes and control characters are present
    return ''.join(c for c in input_str if c.isalnum() or c in [',', '.', ' ', '-'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.call(["ping", sanitized_host])

    return {"status": "completed"}