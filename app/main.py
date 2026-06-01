from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    # Add your sanitization logic here
    return ''.join(c for c in input_str if c.isalnum() or c in ('-', '.', '_', ':', '@'))

@app.get("/ping")
def ping(host: str):

    # Sanitize the input before using it in the command
    sanitized_host = sanitize_input(host)

    # Use subprocess.run instead of subprocess.call and avoid shell=True
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)

    return {
        "status": "completed",
        "output": result.stdout
    }