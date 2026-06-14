from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if re.match(r'^[a-zA-Z0-9.-_]+$', sanitized_host):  # Add regex to validate host format
        args = ['ping', shlex.quote(sanitized_host)]
        try:
            subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "output": subprocess.check_output(args).decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        raise ValueError("Invalid host")