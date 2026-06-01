from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    try:
        if not validate_host(host):
            raise ValueError('Invalid host')
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    except ValueError as e:
        return {'error': str(e)}
    return {'status': 'completed'}