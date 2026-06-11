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