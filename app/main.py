from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid input'}
    host = shlex.quote(host)
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, shlex.Error) as e:
        return {'status': 'failed', 'error': str(e)}