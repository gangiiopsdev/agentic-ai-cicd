from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Simple sanitization logic
    return input_string.replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}