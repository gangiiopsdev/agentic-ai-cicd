from fastapi import FastAPI
import subprocess
global pings = set()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in pings:
        pings.add(host)
        subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}