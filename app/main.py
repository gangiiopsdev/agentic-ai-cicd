from fastapi import FastAPI
import subprocess
import shlex
import re

class CommandLineInjectionException(Exception):
    pass

app = FastAPI()

def secure_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise CommandLineInjectionException("Invalid input")
    args = ['ping', *shlex.split(host)]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}

@app.get="/ping")
def ping(host: str):
    return secure_ping(host)