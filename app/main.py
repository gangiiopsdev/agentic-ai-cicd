from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def ping(host: str):
    if not os.path.exists('/bin/ping'):
        return {'status': 'failed', 'error': 'ping command not found'}
    try:
        result = subprocess.run(['/bin/ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}