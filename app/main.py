from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))

def validate_host(host):
    # Basic validation to prevent common attacks
    if host.startswith('.') or '..' in host:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        sanitized_host = sanitize_input(host)
        command = ['ping', shlex.quote(sanitized_host)]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode(), 'error': ''}
    except ValueError as e:
        return {'status': 'failed', 'output': '', 'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': '', 'error': e.stderr.decode()}