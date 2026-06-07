from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    return ''.join(c for c in user_input if c.isalnum() or c.isspace())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', *shlex.split(sanitized_host)]
    subprocess.run(command, check=True, shell=False)
    return {"status": "completed"}