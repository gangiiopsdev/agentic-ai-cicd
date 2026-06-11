from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.ping_command = ['ping', '{}']

app = FastAPI()

def is_valid_host(host):
    # Basic validation for demonstration purposes
    return host.replace('.', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        service = PingService()
        subprocess.run(service.ping_command + [host], check=True)
    else:
        raise ValueError('Invalid host')

    return {'status': 'completed'}