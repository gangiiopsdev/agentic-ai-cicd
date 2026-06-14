from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input_str if c in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        # Validate and sanitize the input
        if not sanitized_host or ' ' in sanitized_host or '@' in sanitized_host:
            raise ValueError('Invalid host input')
        subprocess.run(['ping', '-c', '1'] + shlex.split(sanitized_host), check=True)
        return {'status': 'completed'}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'error', 'message': str(e)}