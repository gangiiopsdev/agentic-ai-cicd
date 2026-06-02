from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if not is_valid_host(host):
        return{"error": "Invalid host"}, 400
    PingCommand(['ping', host])
    return {"status": "completed"}

import re
def is_valid_host(host: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))