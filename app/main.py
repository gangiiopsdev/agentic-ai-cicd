from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app.get('/ping')(ping)