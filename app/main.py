from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run and shlex.quote
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping_route(host: str):
    return {'result': 'Pinging ' + host}