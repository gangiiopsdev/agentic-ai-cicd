from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the input host to prevent command injection
        if not all(c.isalnum() or c in '-.' for c in host):  # Allow alphanumeric, hyphen, and dot
            return {'status': 'failed', 'error': 'Invalid hostname'}
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr)}