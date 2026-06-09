from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate the host input to ensure it does not contain malicious content
        if not host.isalnum():
            return {'status': 'failed', 'error': 'Invalid host input'}
        subprocess.call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}