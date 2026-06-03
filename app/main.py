from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    args = ['ping', host]
    subprocess.call(args, shell=False)