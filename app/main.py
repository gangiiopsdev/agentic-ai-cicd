from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True, shell=False)

@app.get('/ping')
def ping(host: str):
    # Safe implementation using shlex.quote to escape command arguments
    safe_ping(host)
    return {'status': 'completed'}