from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host], shell=False)
    return {'status': 'completed'}