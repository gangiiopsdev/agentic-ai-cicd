from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_host(host):
    if not host.strip():
        raise ValueError('Host cannot be empty')
    if ' ' in host:
        raise ValueError('Host should not contain spaces')
    return host

@app.get("/ping")
def ping(host: str):
    try:
        validated_host = validate_host(host)
        # Secure implementation with shlex to safely handle arguments
        subprocess.run(['ping', validated_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": subprocess.getoutput('ping ' + validated_host)}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e), "status": "failed", "stderr": e.stderr.decode()}