from fastapi import FastAPI
import subprocess
import re
class SanitizedHost:
    def __init__(self, host: str):
        self.host = subprocess.list2cmdline([host])
        if not re.match(r'^[a-zA-Z0-9.-]+$', self.host):
            raise ValueError("Invalid host")

app = FastAPI()

def safe_ping(host: SanitizedHost):
    subprocess.run(['ping', '-c', '1', host.host], shell=False, check=True)

@app.get('/ping')
def ping(host: str):
    safe_ping(SanitizedHost(host))
    return {'status': 'completed'}