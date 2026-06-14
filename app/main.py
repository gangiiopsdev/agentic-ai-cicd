from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host != '127.0.0.1':
        return {'error': 'Invalid host'}
    subprocess.run(['ping', '-c', '4', '127.0.0.1'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}