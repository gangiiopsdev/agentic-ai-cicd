from fastapi import FastAPI
import subprocess
from os.path import abspath

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with absolute path and shell=False
    try:
        subprocess.run([abspath('ping'), host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}