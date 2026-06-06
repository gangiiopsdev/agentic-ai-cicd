from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingCommand(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v:
            raise ValueError('Host is required')
        return v.strip()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host=host)
    try:
        result = await asyncio.create_subprocess_exec('ping', ping_command.host, capture_output=True, text=True)
        return {'status': (await result.stdout.read()).decode()}
    except subprocess.CalledProcessError as e:
        return {'status': f'Ping failed: {e.output.decode()}'}