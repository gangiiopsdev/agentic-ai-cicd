from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Simple sanitization logic
    return input_string.replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation with shell=False and using check=True for error handling
    try:
        subprocess.run(['ping', sanitized_host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}