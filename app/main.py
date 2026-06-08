from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_str))
def validate_host(host):
    if host.startswith('.') or '..' in host:
        raise ValueError('Invalid hostname')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        sanitized_host = sanitize_input(host)
        args = ['ping', sanitized_host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}