from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

global_args = {"host": "8.8.8.8"}

@app.get('/ping')
def ping(host: str = None):
    if not host:
        host = global_args['host']
    cmd_parts = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(cmd_parts, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive controls
- Validate and sanitize user input before using it in subprocess calls.
- Use safer alternatives like `subprocess.run` with `shell=False` and properly escape arguments.