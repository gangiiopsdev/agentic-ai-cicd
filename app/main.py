from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingCommand(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(ping_command: PingCommand):
    # Sanitize the input to avoid command injection
    sanitized_host = subprocess.quote(ping_command.host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'result': result.stdout}