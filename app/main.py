from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here (e.g., allow only certain characters)
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(filter(allowed_chars.__contains__, input_string))
    return sanitized

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input sanitization and explicit path to ping
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['/bin/ping', sanitized_host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Add additional validation to ensure the host is a valid IP address or hostname