from fastapi import FastAPI
import subprocess
global host_list
host_list = ['example.com', 'google.com']

def check_host(host):
    return host in host_list

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not check_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=5)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except TimeoutExpired:
        return {'status': 'timeout', 'message': 'Ping command timed out'}