from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.strip() or not cls.is_valid_hostname(v):
            raise ValueError('Invalid hostname')
        return v

    @staticmethod
def is_valid_hostname(hostname):
        # Basic validation of a hostname
        if len(hostname) > 255:
            return False
        if hostname[-1] == '.':
            hostname = hostname[:-1]
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.")
        return all(char in allowed_chars for char in hostname)

@app.get('/ping')
def ping(request: PingRequest):
    host = request.host
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'result': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'result': str(e)}