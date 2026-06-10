from fastapi import FastAPI
import subprocess
import string
import os
import secrets

app = FastAPI()

def ping(host: str):
    payload = 'ping' + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))
    args = [payload, host]
    subprocess.run(args, check=True)
    return {"status": "completed"}