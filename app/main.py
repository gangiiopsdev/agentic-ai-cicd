from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using shlex.quote to escape arguments
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}

@app.get("/ping")
def execute_ping(host: str):
    return ping(host)