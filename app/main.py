from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com']

def validate_host(host):
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        args = ['ping', host]
        process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'result': process.stdout}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}