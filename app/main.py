from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and input validation
    if not host.strip():
        return {'status': 'error', 'message': 'Host is empty'}
    result = subprocess.run(['/bin/ping', '-c', '1', host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}