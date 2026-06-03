from fastapi import FastAPI
import subprocess
import shlex
def is_safe_host(host):
    safe_hosts = ['localhost', '127.0.0.1']
    return host in safe_hosts
class SafePing:
    def __call__(self, host: str):
        if not is_safe_host(host):
            raise ValueError('Unsafe host')
        command = shlex.split(f'ping -c 1 {host}')
        result = subprocess.run(command, check=True, capture_output=True)
        return result.stdout.decode()
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        output = SafePing()(host)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'error': str(e)}