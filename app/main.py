from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if host not in ['localhost', '127.0.0.1']:
        return {'error': 'Invalid host'}
    # Use subprocess.run instead of subprocess.call and specify shell=False
    try:
        result = subprocess.run(['ping'], capture_output=True, text=True)
        return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)