from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host: str) -> str:
    return ''.join(c for c in host if c.isalnum())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and escape the host input
        escaped_host = escape_host(host)
        result = subprocess.run(shlex.split(f'ping {escaped_host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}