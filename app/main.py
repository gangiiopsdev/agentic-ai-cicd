from fastapi import FastAPI
import subprocess
import shlex
import re

global ALLOWED_HOSTS = set(['example.com', 'test.com'])  # Define allowed hosts

app = FastAPI()

def escape_command_arg(arg):
    return shlex.quote(arg)

@app.get("/ping")
def ping(host: str):
    if host.isalnum() and host in ALLOWED_HOSTS:
        subprocess.call(['ping', escape_command_arg(host)])
    else:
        return {'status': 'invalid input'}
    return {'status': 'completed'}