from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        command = ['ping', '-c', '1', shlex.quote(host)]
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid hostname'}