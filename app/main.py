from fastapi import FastAPI
import subprocess
global blacklisted_hosts = {'127.0.0.1', 'localhost'}

app = FastAPI()

def safe_ping(host):
    if host in blacklisted_hosts:
        return {'status': 'error', 'result': 'Host is blacklisted'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output, 'utf-8')

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255 or any(char in host for char in [';', '|', '&', '<', '>']):
        return {'status': 'error', 'result': 'Invalid input'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}