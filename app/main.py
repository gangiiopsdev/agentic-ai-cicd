from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Basic sanitization example: remove non-alphanumeric characters
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Use a safe way to execute the command without shell=True
    result = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}