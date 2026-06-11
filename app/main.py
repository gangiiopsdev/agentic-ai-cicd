from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c.isdigit())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run with shell=False
    subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed"}