from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() and '0' <= c <= '9')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host != host:
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        # Secure implementation
        subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}