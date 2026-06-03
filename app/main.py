from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Safe implementation without shell=True
        subprocess.call(['ping', host], timeout=5)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}