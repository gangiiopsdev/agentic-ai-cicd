from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Safer implementation using subprocess.run with validated input
        if host.strip().isdigit() and len(host) <= 3:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': 'Invalid input'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}