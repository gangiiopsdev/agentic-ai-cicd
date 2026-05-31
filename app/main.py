from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'error', 'error': 'Unauthorized host'}
    try:
        subprocess.call(['ping', host])
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)