from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Implement proper input validation and sanitization
    return ''.join(c for c in host if c.isalnum() or c in ['-', '.'])

@app.get("/ping")
def ping(host: str):

    # Sanitize the input before passing it to subprocess
    sanitized_host = sanitize_host(host)

    # Use subprocess.call with a list of arguments instead of shell=True
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}