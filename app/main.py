from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Add your list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', host], shell=False, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get('/ping')
def ping_endpoint(host: str):
    response = ping(host)
    return {'status': 'completed', 'response': response}