from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host parameter
        if not host.strip().isalnum():
            return {'status': 'failed', 'error': 'Invalid host name'}
        # Secure implementation using subprocess.Popen
        subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}