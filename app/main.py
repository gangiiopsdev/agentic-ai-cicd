from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        subprocess.run(['ping', '-c', '1', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}