from fastapi import FastAPI
import subprocess
import re
def sanitize_input(input_string):
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if pattern.match(input_string):
        return input_string
    else:
        raise ValueError("Invalid input")
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', shlex.quote(sanitized_host)]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}