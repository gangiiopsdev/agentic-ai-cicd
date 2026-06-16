from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with shell=False and full path
    try:
        subprocess.call(['/bin/ping', host], timeout=5)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}