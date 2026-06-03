from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Simple sanitization example: allow only alphanumeric characters and periods
    return ''.join(char for char in input_str if char.isalnum() or char == '.')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, capture_output=True)
    return {"status": "completed"}