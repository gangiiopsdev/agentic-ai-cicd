from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host is not allowed'}

    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)