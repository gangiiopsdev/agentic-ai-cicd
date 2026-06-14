from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

global_config = {'ping_path': '/bin/ping'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        try:
            subprocess.run([global_config['ping_path'], host], check=True, shell=False)
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Invalid host'}

    return {'status': 'completed'}