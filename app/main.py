from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return input_string.strip().replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):

    # Sanitize the input to prevent command injection
    sanitized_host = sanitize_input(host)

    # Use subprocess.run with proper argument parsing for a safer implementation
    subprocess.run(['ping', sanitized_host], capture_output=True, text=True)

    return {"status": "completed"}