from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Add more allowed hosts as needed
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Host not allowed for ping operation')

@app.get("/ping")
def ping(host: str):
    try:
        status = safe_ping(host)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}