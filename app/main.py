from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'output': 'Invalid input'}
    try:
        result = subprocess.run(shlex.split('ping -c 1 ' + shlex.quote(host)), capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': str(e)}
    return {'status': 'completed', 'output': result.stdout}