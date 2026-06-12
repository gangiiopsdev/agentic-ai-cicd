from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    safe_hosts = ['127.0.0.1', '::1']
    return host in safe_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if is_safe_host(host):
        try:
            subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'result': 'Ping successful'}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Unsafe host'}