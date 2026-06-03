from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    if not isinstance(input, str) or not input.strip():
        raise ValueError("Invalid input")
    return ''.join(c for c in input if c.isalnum() or c in ['.', '-', '_'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=True)
    return {"status": "completed"}