from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host):
    if not host or ' ' in host:
        return {'error': 'Invalid host'}, 400
    try:
        output = subprocess.check_output(['ping', '-c', '1', quote(host)], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'error': str(e.output)}, 500

class PingRouter:
    @app.get('/ping')
    def ping(host: str):
        return safe_ping(host)