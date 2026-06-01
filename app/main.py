from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Implement input sanitization logic here
    return ''.join(c for c in input_str if c.isalnum() or c in (',', '.', ':'))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}