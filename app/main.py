from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def ping(host: Optional[str] = None):
    if host and host.isalnum():
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid input'}