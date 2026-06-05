from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize the host input to avoid command injection
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            return {'status': 'failed', 'error': 'Invalid host name'}
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}