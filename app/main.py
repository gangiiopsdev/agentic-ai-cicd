from fastapi import FastAPI
import subprocess
def ping_host(host):
    if not host:
        return {'status': 'error', 'message': 'Host parameter is missing'}
    try:
        gtfo = subprocess.run(['ping', '-c', str(1), '--', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': gtfo.stdout, 'errors': ''}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()
app.get('/ping')(ping_host)