from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = shlex.split('ping ' + host)
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}