from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input by checking for potentially harmful characters
    if any(char in host for char in [';', '&', '|', '`', '$']):
        return {'error': 'Invalid input'}
    command = ['ping', host]
    subprocess.call(command)
    return {'status': 'completed'}