from fastapi import FastAPI
import subprocess
from fastapi import HTTPException
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip().isdigit() or len(host.split('.')) != 4:
        raise HTTPException(status_code=400, detail='Invalid host format')
    subprocess.call(['ping', '-c', '1', quote(host)])
    return {'status': 'completed'}