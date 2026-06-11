from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Basic sanitization
    return ''.join(c for c in input_string if c.isalnum() or c in ['-', '.', '_'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}