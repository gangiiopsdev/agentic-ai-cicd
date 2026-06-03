from fastapi import FastAPI
import subprocess
import shlex
from fastapi.responses import JSONResponse
import re

app = FastAPI()

def sanitize_input(input_string):
    # Add proper sanitization logic here
    return re.sub(r'[^a-zA-Z0-9-\.\_\:]', '', input_string)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        args = shlex.split(f'ping -c 1 {sanitized_host}')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return JSONResponse(content={"status": "completed", "result": result.stdout}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "failed", "error": e.stderr}, status_code=500)