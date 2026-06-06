from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host:
        return None
    try:
        subprocess.call(['ping', '-c', '1', host])
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)