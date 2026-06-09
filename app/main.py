from fastapi import FastAPI
import subprocess
from typing import List
class CommandExecutor:
    @staticmethod
def run(command: List[str]):
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using CommandExecutor
    command = ['ping', host]
    if not host.strip():
        raise ValueError('Host parameter cannot be empty')
    return CommandExecutor.run(command)