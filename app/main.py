from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get("/ping")
def ping(host: str):    
    if not PingRequest(host).is_valid_host():
        return {'error': 'Invalid host'}
    subprocess.call(['ping', subprocess.list2cmdline([host])])  # Use list2cmdline to properly escape command line arguments
    return {'status': 'completed'}
class PingRequest:
    def __init__(self, host: str):
        self.host = host
    def is_valid_host(self):
        # Basic validation to check if the host contains only alphanumeric characters and hyphens
        return all(c.isalnum() or c == '-' for c in self.host)