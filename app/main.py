from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = r'^[a-zA-Z0-9.-]+$'
    return re.match(allowed_chars, input_string).group() if re.match(allowed_chars, input_string) else ''

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "error", "message": "Invalid host name"}
    command = ['ping', sanitized_host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}