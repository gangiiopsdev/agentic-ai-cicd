from fastapi import FastAPI
import subprocess
import re
class SanitizedHost:
    def __init__(self, host: str):
        self.host = subprocess.list2cmdline([host])
        if not re.match(r'^[a-zA-Z0-9.-]+$', self.host):
            raise ValueError("Invalid host")

app = FastAPI()

async def safe_ping(host: SanitizedHost):  # Use async to avoid blocking the event loop
    try:
        await subprocess.run(['ping', '-c', '1', host.host], shell=False, check=True)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(SanitizedHost(host))
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}, 400