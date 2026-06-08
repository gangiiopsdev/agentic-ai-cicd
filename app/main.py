from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': jsonable_encoder(e.output)}