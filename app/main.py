from fastapi import FastAPI
import shlex
from subprocess import Popen, PIPE
gapp = FastAPI()

@gapp.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.strip():
        return {'status': 'error', 'message': 'Invalid input'}
    args = shlex.split(f"ping {host}")
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    if error:
        return {'status': 'error', 'message': error.decode()}
    return {'status': 'completed', 'output': output.decode()}