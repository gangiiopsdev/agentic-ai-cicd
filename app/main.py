from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Safe implementation using subprocess.run and checking for common errors
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}