from fastapi import FastAPI
import subprocess
class SanitizedInput:
    def __init__(self, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'):
        self.allowed_chars = set(allowed_chars)

    def __call__(self, value):
        return ''.join(c for c in value if c in self.allowed_chars)

app = FastAPI()
sanitized_input = SanitizedInput()
def ping(host: str = sanitized_input()):
    try:
        output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, timeout=10, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_wrapper(host: str = sanitized_input()):
    return ping(host)