from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):  
    return {'status': 'completed', 'result': ping_safe(host)}