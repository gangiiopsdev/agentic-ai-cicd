from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '-', '_'))

def safe_ping(host: str):
    if not host.strip():
        raise ValueError("Invalid host")
    command = ["ping", *shlex.split(host)]
    subprocess.run(command, shell=False)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}