from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    try:
        subprocess.call(['ping', host], timeout=5)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}