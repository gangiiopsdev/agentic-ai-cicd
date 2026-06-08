from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    args = ['ping', host]
    if subprocess.call(args, shell=False) != 0:
        return 'Ping failed'
    else:
        return 'Ping successful'

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)