from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c == '.' or c == ':')
cmd = ['ping', host]
ping_cmd = shlex.split(' '.join(cmd))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Validate and sanitize host input
    if not host:
        raise ValueError("Invalid host input")
    subprocess.run(ping_cmd, check=True, shell=False)
    return {"status": "completed"}