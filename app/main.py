from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Use a whitelist of allowed hosts to prevent command injection
        if host not in ['google.com', 'example.com']:
            return {'status': 'failed', 'error': 'Invalid host'}
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}