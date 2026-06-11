from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join([char for char in input_string if char in allowed_chars])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input before using it in subprocess command
    if not all(char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' for char in host):
        return {'error': 'Invalid characters in host'}, 400
    sanitized_host = host
    command = ['ping', sanitized_host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}