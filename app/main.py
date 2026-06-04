from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    subprocess.call(args, shell=False)

@app.get('/ping')
def ping_fixed(host: str):
    args = ['ping', host]
    subprocess.run(args, shell=False)
    return {'status': 'completed'}