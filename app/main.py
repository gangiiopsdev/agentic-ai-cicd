from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    result = {'status': 'completed'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        result['output'] = output.stdout
    except subprocess.CalledProcessError as e:
        result['error'] = str(e)
    return result