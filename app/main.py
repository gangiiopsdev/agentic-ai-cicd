from fastapi import FastAPI
import subprocess
gt
app = FastAPI()

def ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call for better control and security
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}