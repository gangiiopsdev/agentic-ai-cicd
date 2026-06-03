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
        output = subprocess.run(['ping', shlex.quote(escaped_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}