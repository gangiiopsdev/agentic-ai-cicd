from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ['-', '.', '_', ''])

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.Popen
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}