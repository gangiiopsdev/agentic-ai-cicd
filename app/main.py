from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def ping(host: str):
    # Safe implementation using shlex.split for proper argument handling
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}