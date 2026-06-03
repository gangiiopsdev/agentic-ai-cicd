from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        args = shlex.split('ping {}
'.format(shlex.quote(host)))
        output = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}