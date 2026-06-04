from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Enhanced validation of host input to allow only alphanumeric characters, dots, and hyphens
    if not all(c.isalnum() or c in '.-' for c in host):  # Basic validation of host
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

# Add more preventive controls here such as limiting the context in which the subprocess runs or using a safer alternative like `ping3` library.