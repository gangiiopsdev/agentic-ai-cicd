from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', '-c', '1'], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}