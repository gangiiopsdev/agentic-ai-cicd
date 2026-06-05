from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or host.startswith('-'):
        return {'error': 'Invalid input'}, 400
    command = ['ping', f'"{host}"']
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': result.stdout}