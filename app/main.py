from fastapi import FastAPI
import subprocess
import shlex
global host_list
host_list = ['8.8.8.8', '8.8.4.4']
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if host not in host_list:
        return {'error': 'Invalid host'}
    # Secure implementation
    cmd = ['ping', host]
    subprocess.call(cmd)
    return {'status': 'completed'}