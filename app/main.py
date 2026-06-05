from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = {'localhost', '127.0.0.1'}
    if host.strip() in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
    else:
        raise ValueError('Unsafe ping request')

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}