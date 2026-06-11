from fastapi import FastAPI
import subprocess
import shlex
def safe_command(args):
    return subprocess.run(['ping', args], capture_output=True, text=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):    try:
        if not host.isalnum():
            raise ValueError('Invalid host name')
        result = safe_command(shlex.quote(host))
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}