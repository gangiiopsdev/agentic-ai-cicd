from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        subprocess.call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}