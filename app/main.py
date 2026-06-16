from fastapi import FastAPI
import subprocess
from pydantic import validator

global host_list
host_list = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    @validator('host')
    def validate_host(v):
        if v not in host_list:
            raise ValueError("Invalid host")
        return v

    result = subprocess.run(['ping', '-c', '1', v], capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}