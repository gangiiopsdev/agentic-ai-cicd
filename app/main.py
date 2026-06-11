from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to avoid shell injection
    if not host.isalnum() or len(host) > 64:
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        # Use shlex.split to safely handle the command arguments
        args = shlex.split('ping -c 1 ' + host)
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}