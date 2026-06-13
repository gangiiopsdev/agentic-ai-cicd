from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    safe_host = subprocess.list2cmdline([host])
    args = ['ping', safe_host]
    subprocess.run(args, check=True)

@app.get('/ping')
def ping(host: str):
    execute_ping(host)
    return {'status': 'completed'}