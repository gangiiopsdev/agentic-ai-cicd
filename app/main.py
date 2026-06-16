from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    # Use check_output for better error handling and return value
    result = subprocess.check_output(command, stderr=subprocess.STDOUT)
    return {'status': 'completed', 'result': result.decode('utf-8')}