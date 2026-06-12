from fastapi import FastAPI
import subprocess
import shlex

global ALLOWED_HOSTS = {'example.com', 'localhost'}

app = FastAPI()

def sanitize_input(user_input):
    return shlex.quote(user_input)

@app.get('/ping')
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        raise HTTPException(status_code=400, detail='Invalid host')
    sanitized_host = sanitize_input(host)
    command = ['ping', sanitized_host]
    process = subprocess.Popen(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}