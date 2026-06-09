from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '192.168.1.1']  # Example allowed hosts
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.run(args, check=True, text=True)
    else:
        return {'status': 'error', 'message': 'Invalid input'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'status' in result:
        return result
    else:
        return {'status': 'completed'}