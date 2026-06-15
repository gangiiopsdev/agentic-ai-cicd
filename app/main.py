from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command, *args):
    command_parts = shlex.split(command)
    command_parts.extend(args)
    subprocess.call(command_parts)

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if host in ['127.0.0.1', '::1']:  # Allow only localhost access for demonstration purposes
        safe_subprocess('ping', host)
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Access denied"}