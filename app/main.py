from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using a safe command and avoiding shell=True
    try:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500