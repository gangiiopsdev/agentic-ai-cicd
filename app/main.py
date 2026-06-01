from fastapi import FastAPI
import subprocess
cimport os

allowed_hosts = {"example.com", "test.example.com"}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail='Invalid host')
    subprocess.call(['ping', '-c', '1', host])
    return {'status': 'completed'}