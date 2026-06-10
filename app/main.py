from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.'))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    args = ['ping', shlex.quote(safe_host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}