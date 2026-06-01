from fastapi import FastAPI
import shlex

def is_safe_host(host):
    safe_hosts = ['localhost', '127.0.0.1']
    return host in safe_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host')
    args = ['/bin/ping', '-c', '1'] + shlex.split(host)
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}