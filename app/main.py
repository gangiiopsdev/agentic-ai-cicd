from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    subprocess.run(command, check=True, shell=False)

@app.get('/ping')
def ping_endpoint(host: str):
    result = ping(host)
    return {'status': 'completed'}