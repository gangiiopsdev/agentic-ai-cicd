from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with shell=False and arguments properly quoted
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}