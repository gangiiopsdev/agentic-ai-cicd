from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(allowed_chars.__contains__, input_str))

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to ensure it does not contain malicious commands
    sanitized_host = sanitize_input(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):  # Basic regex for a valid hostname/IP
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', '-c', str(1), shlex.quote(sanitized_host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}