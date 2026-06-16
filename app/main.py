from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

# Sanitize the input to avoid injection attacks
import re
def sanitize_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')

global_safe_ping = SafePing.safe_ping

app = FastAPI()

@app.get("/ping")
def ping(host: str):