from fastapi import FastAPI
import subprocess
cimport shlex
from subprocess import Popen, PIPE

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize user input to prevent command injection
    if not host.isalnum() or len(host) > 64:
        return {'error': 'Invalid host'}, 400

    # Use Popen for safer subprocess execution
    process = Popen(['ping', shlex.quote(host)], stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    if error:
        return {'error': error.decode('utf-8')}, 500
    else:
        return {'status': 'completed'}