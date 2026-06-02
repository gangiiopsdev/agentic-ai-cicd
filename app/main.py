from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    if not all(c.isalnum() or c in '-.' for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        args = shlex.split(f'ping {host}')  # Use f-string instead of str.format()
        result = subprocess.run(['ping'] + args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)