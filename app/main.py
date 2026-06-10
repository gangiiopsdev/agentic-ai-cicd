from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Host not allowed')

def safe_subprocess(command, *args):
    full_command = [command] + list(args)
    subprocess.run(full_command, check=True)

@app.get('/ping')
def ping(host: str):
    try:
        if validate_host(host):
            safe_subprocess('ping', host)
    except Exception as e:
        return {'error': str(e)}

    return {'status': 'completed'}