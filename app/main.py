from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in '-_:.')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    subprocess.call(['ping', shlex.quote(safe_host)])
    return {"status": "completed"}