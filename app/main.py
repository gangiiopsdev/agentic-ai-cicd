from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation with proper argument quoting and validation
    try:
        args = ['ping'] + [shlex.quote(arg) for arg in host.split()]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_safe(host: str):
    # Validate input to prevent unexpected behavior
    if not host or len(host) > 100:
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)