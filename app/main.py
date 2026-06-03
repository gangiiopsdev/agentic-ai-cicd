from fastapi import FastAPI
import subprocess
from fastapi.params import Query
import re
cmd_whitelist = ['ping']
arg_whitelist = ["-c", "-w"]
app = FastAPI()

@app.get("/ping")
def ping(host: str = Query(..., min_length=1, max_length=255), count: int = Query(4, le=10), wait_time: int = Query(1, ge=1)):
    # Validate the input to only allow alphanumeric and a few special characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        # Use a whitelist of allowed commands and arguments
        command = [cmd for cmd in cmd_whitelist if cmd == 'ping']
        args = [arg for arg in arg_whitelist if arg in ['-c', '-w']] + [str(count), str(wait_time), host]
        output = subprocess.check_output(command + args, stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}