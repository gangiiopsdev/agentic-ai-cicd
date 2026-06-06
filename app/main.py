from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'stdout': result.stdout.decode('utf-8'), 'stderr': result.stderr.decode('utf-8')}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'status' in result:
        return result
    else:
        return {'status': 'completed', 'stdout': result['stdout'], 'stderr': result['stderr']}