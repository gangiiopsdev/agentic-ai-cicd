from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Enhanced validation and sanitization
    if not host.isnumeric() or len(host) > 15:
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', '-c', '1', shlex.quote(host)]
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}