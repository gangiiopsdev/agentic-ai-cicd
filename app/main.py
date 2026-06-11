from fastapi import FastAPI
import subprocess
from typing import Union


generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str) -> Union[dict, dict]:
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid host name'}

    try:
        subprocess.run(generate_ping_command(host), shell=False, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': str(e)}

    return {'status': 'completed'}