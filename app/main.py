from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in [' ', '.', '-'])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    if not host.strip():
        raise ValueError('Host parameter is empty or invalid')
    subprocess.run(['ping', *host.split()], check=True, shell=False)
    return {'status': 'completed'}