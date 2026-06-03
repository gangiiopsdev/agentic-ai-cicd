from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['.', '-', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safer implementation
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}