from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote
from typing import Optional

app = FastAPI()

def sanitize_input(input_str: str) -> str:
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_', '/'))

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is None:
        return {"status": "No host provided"}
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', shell_quote(sanitized_host)], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}