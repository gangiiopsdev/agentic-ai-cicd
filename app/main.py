from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ' .-')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation using subprocess.run
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}