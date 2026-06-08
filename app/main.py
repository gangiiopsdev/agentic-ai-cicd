from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

def ping(host: str):
    if not socket.gethostbyname_ex(host)[0]:
        return {'status': 'invalid_host'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)