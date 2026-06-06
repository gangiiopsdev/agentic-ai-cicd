from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Using check_output instead of call for better error handling and security
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode('utf-8')}