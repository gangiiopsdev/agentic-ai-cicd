from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and argument unpacking
    try:
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}