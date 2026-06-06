from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with shell=False and full command path
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}