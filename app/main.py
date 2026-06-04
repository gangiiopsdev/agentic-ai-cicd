from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def ping(host: str):
    # Safe implementation using shlex to handle arguments safely
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': 'Pinging host', 'host': host}