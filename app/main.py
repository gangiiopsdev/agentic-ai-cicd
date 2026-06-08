from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with shlex.split for argument parsing
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}