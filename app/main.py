from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get('/ping')
def ping(host: str):
    try:
        safe_host = cmd_quote(escape_host(host))
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'message': 'Ping operation timed out'}