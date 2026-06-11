from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

def validate_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str = Depends(validate_host)):
    try:
        # Use subprocess.run to safely execute the command with a full path
        subprocess.run(['/sbin/ping', '-c', '1', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}