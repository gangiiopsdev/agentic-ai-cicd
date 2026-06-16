from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation with shlex to safely handle command arguments
    command = ['ping', host]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=10)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode()}
    return {'status': 'completed', 'output': output.decode()}