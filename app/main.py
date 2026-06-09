from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join([char for char in input_str if char in allowed_chars])

class InputSanitizer:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = allowed_hosts

    def validate_host(self, host):
        sanitized_host = sanitize_input(host)
        return sanitized_host if sanitized_host in self.allowed_hosts else None

app = FastAPI()

def ping(host: str):
    sanitizer = InputSanitizer(allowed_hosts=['example.com'])
    sanitized_host = sanitizer.validate_host(host)
    if sanitized_host:
        try:
            result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

app.get('/', response_model=dict)
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

app.get('/ping', response_model=dict)
def ping(host: str):
    return ping(host)