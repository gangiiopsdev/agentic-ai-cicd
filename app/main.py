from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return {'status': 'completed'}
        else:
            return {'error': result.stderr}
    except subprocess.TimeoutExpired as e:
        return {'error': str(e)}