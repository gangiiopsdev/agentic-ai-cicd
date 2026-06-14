from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host: str):
    if not host.isdigit():
        return 'Invalid host'
    args = ['ping', '-c', '1', shlex.quote(host)]  # Use shlex.quote to escape user input
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get('/ping')
def ping(host: str):
    if not all(c.isdigit() for c in host):
        return {'status': 'error', 'message': 'Invalid host'}
    output = run_ping(host)
    return {'status': 'completed', 'output': output}