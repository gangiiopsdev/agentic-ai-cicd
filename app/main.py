from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' + chr(9) * 2  # Allow common special characters for hostnames/IP addresses
    return ''.join(char for char in host if char in allowed_chars)
def quote_command(args):
    return [quote(arg) for arg in args]
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host != host:
        return {"status": "invalid host", "message": "Host contains disallowed characters"}
    subprocess.run(quote_command(["ping", sanitized_host]), check=True, shell=False)
    return {"status": "completed"}