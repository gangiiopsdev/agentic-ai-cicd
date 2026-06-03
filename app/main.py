from fastapi import FastAPI
import subprocess
import ipaddress

global white_listed_hosts = ['127.0.0.1', '::ffff:127.0.0.1']
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return {'status': 'error', 'message': 'Invalid host'}

    if host not in white_listed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}

    # Secure implementation
    command = ['ping', '-c', '4', host]
    subprocess.run(command, check=True, stdout=subprocess.PIPE, shell=False)
    return {'status': 'completed'}