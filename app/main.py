from fastapi import FastAPI
import subprocess
import socket
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate host using socket to ensure it is a valid IP or hostname
        socket.gethostbyname(host)
        result = subprocess.run(['ping', '-c 1'] + shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode('utf-8'), 'stderr': result.stderr.decode('utf-8')}
    except (subprocess.CalledProcessError, socket.gaierror) as e:
        return {'status': 'error', 'message': str(e)}