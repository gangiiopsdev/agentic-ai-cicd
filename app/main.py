from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Basic sanitization to prevent shell injection
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_', '@'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True, capture_output=True)
    return {"status": "completed"}