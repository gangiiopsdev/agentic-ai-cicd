from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output.decode('utf-8')}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic validation to allow only alphanumeric characters
        raise ValueError('Invalid host')
    result = safe_ping(shlex.quote(host))
    return {'status': 'completed', 'result': result}