from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode()}
    return {'status': 'completed', 'output': output.decode()}