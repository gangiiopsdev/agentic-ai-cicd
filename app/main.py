from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter to ensure it only contains safe characters
    safe_host = ''.join(c for c in host if c.isalnum() or c in ('-', '.', '_'))
    try:
        output = subprocess.check_output(shlex.split(f'ping {safe_host}'), stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}