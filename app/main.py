from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True)
    return {'status': 'completed'}