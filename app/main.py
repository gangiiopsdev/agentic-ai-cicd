from fastapi import FastAPI
import subprocess
import shlex
class HostValidator:
    @staticmethod
def validate(host):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validator = HostValidator()
    if not validator.validate(host):
        return {"status": "invalid_host"}
    # Secure implementation using shlex.quote to escape special characters
    subprocess.call(shlex.split(f'ping {shlex.quote(host)}')))
    return {"status": "completed"}