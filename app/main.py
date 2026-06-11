from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(host):
    if not host.replace('.', '').isdigit() and ':' not in host:
        raise ValueError('Invalid host format')

@app.get("/ping")
def ping(host: str):
    try:
        validate_input(host)
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}, 400