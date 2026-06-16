from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return {'status': 'completed'}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)