from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safe implementation using check_output with shell=False and validating host input
    if not all(c.isalnum() or c in '.-' for c in host):  # Basic validation of host
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}