from fastapi import FastAPI
import subprocess
call = subprocess.call

app = FastAPI()

@app.get('/ping')
def ping_safe(host: str):
    if not host.isdigit() and len(host) <= 15:
        call(['ping', host], shell=False)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid input'}, 400