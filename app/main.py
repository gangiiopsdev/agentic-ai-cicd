from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}