from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ['.', '-'])

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    escaped_host = escape_host(host)
    try:
        output = subprocess.check_output(['ping', shlex.quote(escaped_host)], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}