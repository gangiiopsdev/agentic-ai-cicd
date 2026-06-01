from fastapi import FastAPI
import re

def is_safe_host(host):
    safe_hosts = ['localhost', '127.0.0.1']
    pattern = r'^[a-zA-Z0-9.-]+$'
    if not re.match(pattern, host) or host in safe_hosts:
        return True
    raise ValueError('Unsafe host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host')
    subprocess.run(['/bin/ping', '-c', '1', re.escape(host)], check=True, capture_output=True, text=True)
    return {'status': 'completed'}