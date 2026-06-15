from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isdigit() or len(host) > 3:
        return {'error': 'Invalid input'}
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True, capture_output=True)
    return {'status': 'completed'}