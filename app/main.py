from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', shlex.quote(sanitized_host)]
    subprocess.call(args, shell=False)
    return {'status': 'completed'}