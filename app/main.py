from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        try:
            output = subprocess.check_output(['ping', self.host], stderr=subprocess.STDOUT, shell=False)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.output.decode('utf-8')}

class HostModel(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v or len(v) > 255 or not all(c.isalnum() or c in '.-_' for c in v):
            raise ValueError('Invalid host')
        return v

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(HostModel(host=host).host)
    return ping_command.run()

# Add additional security measures to further harden the application
import os
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)