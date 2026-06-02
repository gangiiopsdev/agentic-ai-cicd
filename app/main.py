from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(value):
    if not value.isalnum():
        raise ValueError("Invalid input")

@app.get('/ping')
def ping(host: str):
    try:
        sanitize_input(host)
        args = ['ping', quote(host)]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 400