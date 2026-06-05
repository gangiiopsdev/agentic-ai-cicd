from fastapi import FastAPI
import subprocess
import re
class Ping:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        # Safe implementation
        args = ['ping', self.host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    if not re.match(r'^[a-zA-Z0-9.-]+$', host):\n        return {'error': 'Invalid hostname'}\n    ping_instance = Ping(host)\n    ping_instance.execute()\n    return {"status": "completed"}