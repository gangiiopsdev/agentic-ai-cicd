from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    # Add input validation logic here
    return ''.join(c for c in input_string if c.isalnum() or c in ('.', '-', '_'))

def safe_subprocess(command, *args):
    args = shlex.split(' '.join(map(shlex.quote, args)))
    subprocess.call([command] + args)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    safe_subprocess("ping", sanitized_host)
    return {"status": "completed"}