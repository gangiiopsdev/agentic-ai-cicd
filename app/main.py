from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not host.isalnum() and '-' not in host and '.' not in host and '_' not in host and ' ' not in host:
        raise ValueError('Invalid input')
    return safe_ping(host)