from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_'
    for char in host:
        if char not in allowed_chars:
            return False
    return True
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not validate_host(host) or len(host) > 255:
        return {"status": "failed", "error": "Invalid host name"}
    try:
        output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}