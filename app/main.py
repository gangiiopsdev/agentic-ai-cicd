from fastapi import FastAPI
import subprocess

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_', '/', ':'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Use a safer alternative to subprocess.run for user-provided input
    subprocess.call(['ping', '-c', '1', sanitized_host], check=True, capture_output=True)
    return {"status": "completed"}