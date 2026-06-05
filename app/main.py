from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Use the correct argument format for subprocess.call
        subprocess.call(['ping', host], shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}