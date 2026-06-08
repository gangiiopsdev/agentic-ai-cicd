from fastapi import FastAPI
import subprocess
import re

def sanitize_input(user_input):
    return ''.join(e for e in user_input if re.match(r'[a-zA-Z0-9.-]+', e))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    if not host:
        return {"status": "error", "message": "Invalid input"}
    subprocess.run(shlex.split(f'ping -c 4 {shlex.quote(host)}'), check=True, text=True)
    return {"status": "completed"}