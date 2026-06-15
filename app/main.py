from fastapi import FastAPI, Request
import subprocess
from pydantic import BaseModel
import re

class PingResponse(BaseModel):
    status: str

def sanitize_input(input_string):
    return ''.join(e for e in input_string if re.match(r'[a-zA-Z0-9.-_]', e))

app = FastAPI()

@app.get("/ping")
def ping(request: Request, host: str):
    safe_host = sanitize_input(host)
    command = ['ping', safe_host]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return PingResponse(status=result.stdout)