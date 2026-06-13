from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    allowed_hosts = ['localhost', '127.0.0.1']
    return input_str.strip().lower() in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not sanitize_input(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', shlex.quote(host)]  # Using shlex.quote to safely handle input
    subprocess.run(args, check=True)  # Using subprocess.run with check=True for better error handling
    return {'status': 'completed'}