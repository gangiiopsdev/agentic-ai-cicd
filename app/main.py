from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        return {'status': 'failed', 'message': 'Invalid host name'}
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'message': 'Ping successful'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'message': str(e.output)}