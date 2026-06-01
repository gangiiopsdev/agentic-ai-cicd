from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Secure implementation using subprocess.run with shell=False and validation
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}