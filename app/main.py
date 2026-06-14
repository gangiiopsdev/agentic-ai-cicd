from fastapi import FastAPI
import subprocess
class PingRequest:
    def __init__(self, host: str):
        self.host = host

app = FastAPI()

@app.get("/ping")
def ping(host_str: str):
    if not valid_host(host_str):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', host_str]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def valid_host(host: str) -> bool:
    # Add validation logic for the host
    return True