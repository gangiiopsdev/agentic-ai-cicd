from fastapi import FastAPI
import subprocess
def ping_host(host):
    if not host:
        return {'status': 'error', 'message': 'Host parameter is missing'}
    gtfo = subprocess.Popen(['ping', f'"{host}"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = gtfo.communicate()
    return {'status': 'completed', 'output': out.decode(), 'errors': err.decode()}

app = FastAPI()
app.get('/ping')(ping_host)