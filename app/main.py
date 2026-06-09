from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host in allowed_hosts:
        command = ['ping', host]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    else:
        return {'error': 'Host not allowed'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)