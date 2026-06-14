from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = sanitize_input(host)

    # Use subprocess.run instead of subprocess.call with shell=True
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)

    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }