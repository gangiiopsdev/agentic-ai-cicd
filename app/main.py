from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(shlex.split('ping -c 1 ' + host), check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}