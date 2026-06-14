from fastapi import FastAPI
import subprocess
import shlex

global_args = ['ping']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with shlex to safely handle arguments
    args = global_args + shlex.split(host)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}