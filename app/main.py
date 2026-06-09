from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def sanitize_input(input_string):
    try:
        return ''.join(c for c in input_string if c.isalnum())
    except Exception as e:
        raise ValueError("Invalid input")

@app.get('/ping')
def ping(host: str):\n    sanitized_host = sanitize_input(host)
    command = shlex.split(f'ping {sanitized_host}')
    try:\n        subprocess.run(command, check=True, text=True, capture_output=True)
        return {'status': 'completed'}\n    except subprocess.CalledProcessError as e:\n        return {'error': str(e)}