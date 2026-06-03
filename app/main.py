from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_command(host):
    if not host.isalnum() or len(host) > 64:
        raise ValueError('Invalid hostname')
    command = ['ping', host]
    return command

@app.get('/ping')
def ping(host: str):
    result = subprocess.run(safe_command(host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}