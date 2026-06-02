from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingCommand(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if '&&' in v or ';' in v or '|' in v:
            raise ValueError('Invalid characters in hostname')
        return v

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    command_executor = PingCommand(host=host)\n    try:\n        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n        output, error = await result.communicate()\n        if error:\n            return {'status': 'failed', 'error': error.decode()}\n        else:\n            return {'status': 'completed', 'output': output.decode()}\n    except Exception as e:\n        return {'status': 'failed', 'error': str(e)}