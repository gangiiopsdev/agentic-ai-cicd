from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    if not host:
        return False
    # Use a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return False
    try:
        subprocess.run(['ping', f'"{host}"'], check=True)
        return True
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result == False:
        return {'status': 'failed', 'message': 'Invalid host'}
    else:
        return {'status': 'completed', 'result': result}