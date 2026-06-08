from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def ping(request: PingRequest):
    # Validate input to ensure it does not contain malicious content
    if 'ping' in request.host or ';' in request.host or '&':
        return {'status': 'error', 'message': 'Invalid host name'}
    subprocess.call(["ping", request.host])
    return {'status': 'completed'}