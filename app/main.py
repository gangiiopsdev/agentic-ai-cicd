from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Ensure host is sanitized to prevent injection attacks
        if not host.strip().isalnum():
            return {'error': 'Invalid host'}
        subprocess.run(['/bin/ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}