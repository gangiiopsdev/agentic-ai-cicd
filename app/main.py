from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if 'ping' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        hostname = subprocess.check_output('hostname').decode().strip()
        subprocess.call(['ping', hostname], shell=False)
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}