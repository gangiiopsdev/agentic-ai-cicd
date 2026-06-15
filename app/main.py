from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        args = ['ping', host]
        output = subprocess.run(args, capture_output=True, text=True, timeout=5)
        return output.stdout
    except Exception as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host.isdigit():  # Basic validation to avoid simple command injection
        return {'status': safe_ping(host)}
    else:
        return {'status': 'Invalid host'}