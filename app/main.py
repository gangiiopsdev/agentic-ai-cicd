from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host):
    return subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping(host: str):
    if '&&' not in host and ';' not in host:
        return secure_ping(host)
    else:
        return {'error': 'Invalid input detected'}
    return {'status': 'completed'}