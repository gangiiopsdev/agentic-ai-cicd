from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    destination = 'ping'.format(host)
    cmd = ['ping', host]
    subprocess.call(cmd, shell=False)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)