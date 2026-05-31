from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Ensure host is a trusted input
        if '.' not in host and '@' not in host:
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping'] + shlex.split(host), check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}