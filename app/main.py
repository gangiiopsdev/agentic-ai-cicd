from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    if input_str.strip().lower() in ['localhost', '127.0.0.1']:
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if not sanitize_input(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}