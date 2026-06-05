from fastapi import FastAPI
import subprocess
import re
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join(c for c in host if c in allowed_chars)
    return sanitized_host
class SanitizedSubprocess:
    def call(self, command, **kwargs):
        sanitized_command = subprocess.list2cmdline(command)
        return subprocess.Popen(sanitized_command, **kwargs)
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    sanitized_host = sanitize_host(host)
    subprocess_instance = SanitizedSubprocess()
    subprocess_instance.call(["ping", sanitized_host])
    return {"status": "completed"}