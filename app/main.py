from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()
bearer_scheme = HTTPBearer()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'  # Adjust as needed
    return ''.join(filter(lambda x: x in allowed_chars, input_string))

@app.get("/ping")
def ping(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), host: str = None):
    if not host or len(host) > 255:
        return {'error': 'Invalid host'}, 400
    sanitized_host = sanitize_input(host)
    args = ['ping', subprocess.list2cmdline([sanitized_host])]
    subprocess.call(args, shell=False)
    return {'status': 'completed'}