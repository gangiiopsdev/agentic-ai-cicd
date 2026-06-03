from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        ping_command = ['ping'] + shlex.split(host)
        result = subprocess.run(ping_command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isnumeric():
        raise ValueError('Invalid host input')
    return safe_ping(host)