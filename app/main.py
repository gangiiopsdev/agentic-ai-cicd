from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import Dict

class PingResponse(Dict):
    status: str
    output: str | None = None

app = FastAPI()

def sanitize_input(input_string: str) -> str:
    # Implement input sanitization logic here
    return input_string.strip()

@app.get("/ping")
def ping(host: str) -> PingResponse:
    try:
        sanitized_host = sanitize_input(host)
        output = subprocess.check_output(['ping', '-c', '1', quote(sanitized_host)], timeout=5, text=True)
        return PingResponse(status="completed", output=output)
    except subprocess.CalledProcessError as e:
        return PingResponse(status="error", message=str(e))