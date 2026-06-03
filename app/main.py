from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using check_output for capturing output and avoiding shell=True
    if not host.strip():
        raise ValueError('Host parameter cannot be empty')
    args = ['ping', host]
    try:
        result = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': result.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}