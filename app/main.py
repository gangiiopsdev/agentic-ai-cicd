from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with shell escaping
    subprocess.run(['ping', quote(host)], check=True)
    return {'status': 'completed'}