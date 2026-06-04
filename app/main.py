from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)