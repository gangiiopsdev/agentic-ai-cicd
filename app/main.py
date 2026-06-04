from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ['-', '.', '_', ''])
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.Popen
    sanitized_host = sanitize_input(host)
    subprocess.Popen(['ping', sanitized_host], shell=False, check=True)
    return {'status': 'completed'}