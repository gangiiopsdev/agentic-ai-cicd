from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c.isspace())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}