from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', shlex.quote(sanitized_host)]  # Use shlex.quote to escape special characters
    subprocess.call(command)
    return {"status": "completed"}