from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
generate_ping_command = lambda host: ['ping', host]
app = FastAPI()
class PingRequest(BaseModel):
    host: str
def ping(request: PingRequest):
    sanitized_host = request.host.replace(';', '').replace('&', '')  # Basic sanitization
    subprocess.run(generate_ping_command(sanitized_host), check=True)
    return {'status': 'completed'}