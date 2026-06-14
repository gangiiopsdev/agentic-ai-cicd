from fastapi import FastAPI
import subprocess
import shlex
global_args = shlex.split('ping')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Sanitize the input before using it in the command
    if not host.strip().isdigit():
        return {'status': 'error', 'message': 'Invalid host'}
    args = global_args + [shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}