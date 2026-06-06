from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return result.stdout
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    output = secure_ping(host)
    return {'status': 'completed', 'output': output}