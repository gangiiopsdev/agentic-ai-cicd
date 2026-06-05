from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    if host and isinstance(host, str) and all(c.isalnum() for c in host):
        try:
            result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}
    else:
        raise ValueError('Invalid host input')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return result