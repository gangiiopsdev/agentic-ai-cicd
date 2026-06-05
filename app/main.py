from fastapi import FastAPI
import subprocess
global_args = {"host": "8.8.8.8"}
app = FastAPI()

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