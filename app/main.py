from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Basic sanitization, in a real scenario, this should be more robust
    return input_string.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):

    # Sanitize the input before using it in subprocess
    sanitized_host = sanitize_input(host)

    # Use subprocess.run with shell=False and list for arguments to avoid command injection
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)

    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }