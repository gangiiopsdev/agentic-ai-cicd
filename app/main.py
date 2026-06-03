from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    escaped_host = ''.join(c for c in host if c.isalnum() or c in ['.', '-'])
    try:
        output = subprocess.check_output(['ping', f'-c 1 {shlex.quote(escaped_host)}'], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}