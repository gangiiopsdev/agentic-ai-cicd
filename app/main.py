from fastapi import FastAPI
import subprocess
from pydantic import validator

class HostValidator:
    allowed_hosts = ['example.com', 'another-example.com']  # List of allowed hosts

    @classmethod
    def validate_host(cls, host: str):
        if host not in cls.allowed_hosts:
            raise ValueError('Host is not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str = HostValidator.validate_host()):
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}