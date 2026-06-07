from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', shlex.quote(host)]  # Use shlex.quote to sanitize the user input
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping_endpoint(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid input'}
    return ping(host)