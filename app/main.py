from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in '.-_' for c in host):
        return {'error': 'Invalid host', 'status': 'failed'}
    try:
        subprocess.call(['ping', host], shell=False)
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}
    return {'status': 'completed'}