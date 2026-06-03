from fastapi import FastAPI
import subprocess
import shlex

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
        subprocess.call(shlex.split(f'ping {shlex.quote(validated_host)}'))
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}