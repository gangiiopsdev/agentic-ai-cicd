from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)