from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation with proper argument quoting and input validation
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host name')
    args = ['ping'] + shlex.split(host)
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_safe(host: str):
    return ping(host)