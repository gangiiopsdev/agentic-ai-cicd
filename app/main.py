from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_!@#$%^&*()+=[]{}|;:,.<>?'
    return ''.join(filter(lambda x: x in allowed_chars, host))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr.decode())}