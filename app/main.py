from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_input(input_str):
    # Enhanced sanitization example: remove any characters that are not alphanumeric or common in IP addresses and domain names
    return re.sub(r'[^a-zA-Z0-9.:-]', '', input_str)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', shlex.quote(sanitized_host)]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode == 0:
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "output": result.stderr}