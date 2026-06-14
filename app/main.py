from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import re

app = FastAPI()
bearer_scheme = HTTPBearer()

def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}

    command = ['ping'] + host.split()  # Use double dashes to ensure proper argument handling
    subprocess.run(command, check=True)

    return {'status': 'completed'}