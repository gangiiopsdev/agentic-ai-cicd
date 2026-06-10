from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    try:
        # Use shlex.quote to sanitize the input
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)