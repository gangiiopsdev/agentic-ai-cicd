from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self, host):
        self.host = host
def ping(host: str):
    if not isinstance(host, str) or not host.strip():
        return {'status': 'error', 'output': 'Invalid input'}
    ping_instance = Ping(host)
    result = subprocess.run(['ping', ping_instance.host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}