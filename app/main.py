from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isdigit())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', '-c', '1', sanitized_host], shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}