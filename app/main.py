from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Add input sanitization logic here
    return input_str.strip()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True, text=True)
    return {"status": "completed"}