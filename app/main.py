from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() or e in [ '.', '-', '_' ])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = shlex.split(f"ping {sanitized_host}")
    subprocess.run(command, check=True)
    return {"status": "completed"}