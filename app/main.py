from fastapi import FastAPI
import subprocess
import shlex
def escape_command(input):
    return ''.join(c for c in input if c.isalnum() or c in ['-', '.', ':', '/'])
def validate_host(host):
    try:
        shlex.split(host)
        return True
    except ValueError:
        return False@app.get("/ping")def ping(host: str):    if not validate_host(host):
        return {"status": "invalid host"}, 400    safe_host = escape_command(host)    args = ['ping', '-c', '1', shlex.quote(safe_host)]    subprocess.run(args, check=True)    return {"status": "completed"}