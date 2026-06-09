from fastapi import FastAPI
import subprocess
import re

class Ping:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        # Validate the host input more strictly and ensure it's a valid hostname
        if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', self.host) or '.' not in self.host:
            raise ValueError('Invalid hostname')
        args = ['ping', self.host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host) or '.' not in host:
        return {'error': 'Invalid hostname'}
    try:
        Ping(host).execute()
    except Exception as e:
        return {'error': str(e)}
    return {"status": "completed"}