from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host: str) -> str:
    return host.replace('\', '').replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        escaped_host = escape_host(host)
        command = ['ping'] + shlex.split(escaped_host)
        output = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}