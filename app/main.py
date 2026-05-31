from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host or host.strip() == '':
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True, stdout=subprocess.PIPE)
    return {'status': 'completed'}