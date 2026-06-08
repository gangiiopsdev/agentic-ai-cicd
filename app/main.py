from fastapi import FastAPI
import subprocess
globally_allowed_hosts = ['example.com', 'test.com']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in globally_allowed_hosts:
        subprocess.call(['ping', host], shell=False)
    else:
        raise Exception('Host not allowed')
    return {'status': 'completed'}