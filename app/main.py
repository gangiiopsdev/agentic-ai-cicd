from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}