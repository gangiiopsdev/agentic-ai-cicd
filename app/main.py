from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not host.isalnum() and not all(c in '-.' for c in host):
            return {'status': 'failed', 'error': 'Invalid host name'}
        cmd = ['ping', host]
        args = shlex.split(' '.join(cmd))
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}