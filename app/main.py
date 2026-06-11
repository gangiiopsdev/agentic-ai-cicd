from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if '-' not in host:
        try:
            subprocess.call(['ping', host], shell=False)
        except Exception as e:
            return {'error': str(e)}
    else:
        raise ValueError('Invalid host parameter')
    return {'status': 'completed'}