from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in ['localhost', '127.0.0.1']:
        return {'error': 'Invalid host'}
    # Use subprocess.run instead of subprocess.call and specify shell=False
    try:
        result = subprocess.run(['ping', *shlex.split(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}