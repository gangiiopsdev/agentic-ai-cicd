from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    try:
        command = ['ping', '-c', '1', shlex.quote(host)]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)