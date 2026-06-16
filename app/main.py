from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    command = ['ping', host]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

# Mount the app for testing purposes
global_app = app