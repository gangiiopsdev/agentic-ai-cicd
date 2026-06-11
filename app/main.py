from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    @validator('host')
    def validate_host(v):
        if not v.startswith(('192.168', '172.16', '10.', '::ffff:192.168', '::ffff:172.16', '::ffff:10.')):
            raise ValueError('Invalid host')
        return v

    sanitized_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', sanitized_host], check=True, shell=False)
    return {"status": "completed"}