from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call for better security
        result = subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}