from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def execute_ping(host):
    try:
        # Validate input using a regular expression for allowed hostnames/IP addresses
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return 'Invalid hostname'
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)