from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
app = FastAPI()
@app.get("/ping")
def ping(host: str):\n    validate_host(host)\n    # Secure implementation\n    subprocess.call(['ping', host])\n    return {"status": "completed"}