from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):\n    # Sanitize the host input to prevent command injection\n    safe_host = sanitize_input(host)\n    try:\n        subprocess.run(shlex.split(f"ping -c 1 {safe_host}"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n        return {"status": "completed", "output": stdout.decode()}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": e.stderr.decode()}

def sanitize_input(input_string):\n    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '-', '_'))