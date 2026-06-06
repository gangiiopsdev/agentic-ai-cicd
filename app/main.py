from fastapi import FastAPI
import subprocess
class PingRequest(BaseModel):
    host: str
def ping(host: PingRequest):
    cmd = ['ping', host.host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}