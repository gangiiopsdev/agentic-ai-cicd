from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(lambda x: x in allowed_chars, input_str))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, check=True, capture_output=True, text=True)

    return {'status': 'completed'}