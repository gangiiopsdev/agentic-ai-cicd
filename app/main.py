from fastapi import FastAPI
import subprocess
class SanitizedInput:
    def __init__(self, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'):
        self.allowed_chars = set(allowed_chars)

    def __call__(self, value):
        return ''.join(c for c in value if c in self.allowed_chars)

def validate_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in host)

app = FastAPI()
sanitized_input = SanitizedInput()
def ping(host: str = sanitized_input()):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    try:
        output = subprocess.check_output(['ping', '-c', '4', f'"{host}"'], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_wrapper(host: str = sanitized_input()):
    return ping(host)