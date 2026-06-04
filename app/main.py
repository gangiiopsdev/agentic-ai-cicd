from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(c in allowed_chars for c in host)
def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        args = ['ping', sanitize_input(host)]
        output = subprocess.run(args, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}