from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it is safe for 'ping'
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping {host}')
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return {'status': 'error', 'message': error.decode()}
    else:
        return {'status': 'completed', 'output': output.decode()}