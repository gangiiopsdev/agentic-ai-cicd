from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_input(input_string):
    return input_string.isalnum()

@app.get('/ping')
def ping(host: str):
    if not validate_input(host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}