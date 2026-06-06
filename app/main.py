from fastapi import FastAPI
import subprocess
import shlex
globally_whitelisted_hosts = ['host1', 'host2']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in globally_whitelisted_hosts:
        command = ['ping', '-c 1', host]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Host not allowed')