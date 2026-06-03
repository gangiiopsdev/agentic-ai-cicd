from fastapi import FastAPI
import subprocess
from typing import Union

generate_ping_command = lambda host: ['ping', host]

app = FastAPI()

@app.get('/ping')
def ping(host: str) -> dict:
    try:
        result = subprocess.run(generate_ping_command(host), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e.stderr), 'status': 'failed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}