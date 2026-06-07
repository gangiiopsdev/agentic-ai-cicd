from fastapi import FastAPI
import subprocess
import shlex
global ping_command
canonical_ping_command = ['ping', '{}']

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = canonical_ping_command.copy()
    command[1] = sanitized_host
    subprocess.call(command)
    return {"status": "completed"}