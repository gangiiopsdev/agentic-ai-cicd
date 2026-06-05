from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator, BaseModel

class HostValidator(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.
'
        if any(char not in allowed_chars for char in v):
            raise ValueError(f'Invalid character in host: {v}')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validator = HostValidator(host=host)
    result = subprocess.run(['ping', shlex.quote(validator.host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8')