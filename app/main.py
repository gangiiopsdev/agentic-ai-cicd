from fastapi import FastAPI
import subprocess
guarded_hosts = ['example.com', 'localhost']

app = FastAPI()

def ping(host: str):
    if host not in guarded_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        subprocess.run(['ping', '-c', '1', '--', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)