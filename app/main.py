from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str
def ping(request: PingRequest):
    subprocess.call(['ping', request.host])