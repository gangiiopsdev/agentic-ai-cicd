from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.isalnum():
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}
    return {'status': 'completed'}