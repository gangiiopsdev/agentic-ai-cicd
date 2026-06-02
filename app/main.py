from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingCommand(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, value):
        if not value or not value.isalnum():
            raise ValueError('Invalid host')
        return value

app = FastAPI()

@app.get("/ping")
def ping(host: PingCommand):
    ping_command = PingCommand(host=host.host)
    try:
        output = subprocess.run(['ping', ping_command.host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'result': output.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'result': str(e)}