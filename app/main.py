from fastapi import FastAPI
import subprocess

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit() or e.isspace())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}