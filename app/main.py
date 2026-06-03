from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Simple example of sanitizing input (more comprehensive checks may be needed)
    return ''.join(c for c in input_str if c.isalnum() or c in ('-', '.', ':'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Fixed implementation using subprocess.run with shell=False and properly quoted arguments
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}