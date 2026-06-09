from fastapi import FastAPI
import subprocess
def ping_host(host):
    if not isinstance(host, str) or '&&' in host or ';' in host or '||' in host:
        raise ValueError('Invalid command argument')
    cmd = ['ping', '-c', '1', host]
    result = subprocess.run(cmd, check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode()}

app = FastAPI()
@app.post('/ping/')
def ping(request: dict):
    return ping_host(request['host'])