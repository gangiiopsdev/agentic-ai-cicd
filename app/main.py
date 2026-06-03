from fastapi import FastAPI
import subprocess
from datetime import timedelta
from typing import Dict

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self) -> Dict[str, str]:
        try:
            result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input using a more robust method
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    command = PingCommand(host)
    return command.execute()

def is_valid_host(host: str) -> bool:
    try:
        # Use a more robust method to validate the host
        import socket
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False