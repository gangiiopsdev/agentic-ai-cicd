from fastapi import FastAPI
import re
from subprocess import Popen, PIPE

global allowed_hosts = ['example.com', 'another-example.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        # Use Popen to avoid shell injection risks
        p = Popen(["/bin/ping", host], stdout=PIPE, stderr=PIPE)
        output, error = p.communicate()
        return {"status": "completed", "output": output.decode()} if p.returncode == 0 else {"error": error.decode()}, 400
    else:
        return {"error": "Invalid host"}, 400


def validate_host(host):
    # Implement a more secure and comprehensive host validation logic
    global allowed_hosts
    pattern = r'^[a-zA-Z0-9.-]+$'
    if re.match(pattern, host) and host in allowed_hosts:
        return True
    return False

# Prevent modification of allowed_hosts outside the function