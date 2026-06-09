from fastapi import FastAPI
import subprocess

def ping(host: str):
    call_command = ['ping', host]
    result = subprocess.run(call_command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def sanitized_host_input(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError('Invalid hostname')

app = FastAPI()
@app.get('/ping')
def ping(host: str):