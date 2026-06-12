from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() and e.isascii())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    host = sanitize_input(host)
    if not host:
        raise ValueError("Invalid host name")
    # Use a safe subprocess call with proper shell=False and check=True
    result = subprocess.run(['ping', '-c 1', host], check=True, capture_output=True, text=True, shell=False)
    return {"status": "completed", "output": result.stdout}