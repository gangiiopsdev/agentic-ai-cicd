from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not all(c.isalnum() or c in ['-', '.', '_', ''] for c in host):  # Allow alphanumeric and some special characters
        return {'error': 'Invalid hostname'}, 400

    try:
        subprocess.run(['ping', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 400