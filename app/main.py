from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Sanitize input by allowing only alphanumeric characters and some common IP address formats
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    args = ['ping', shlex.quote(sanitized_host)]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return ping(host)