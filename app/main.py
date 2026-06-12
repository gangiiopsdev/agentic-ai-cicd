from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}