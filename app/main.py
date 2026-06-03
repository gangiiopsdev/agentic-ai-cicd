from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def ping(host: str):
    try:
        # Sanitize host input
        sanitized_host = shlex.quote(host)
        if not os.access(sanitized_host, os.X_OK):
            raise PermissionError(f"Executable file {sanitized_host} does not have execution permissions.")
        subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed'}
    except (subprocess.CalledProcessError, PermissionError) as e:
        return {'status': 'failed', 'output': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)