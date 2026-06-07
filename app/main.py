from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class HostValidator:
    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'localhost']  # Replace with actual allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Invalid host: {v}')
        return v

@app.get("/ping")
def ping(host: str = HostValidator()):
    try:
        output = subprocess.check_output(['ping', subprocess.list2cmdline([host])], stderr=subprocess.STDOUT, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')