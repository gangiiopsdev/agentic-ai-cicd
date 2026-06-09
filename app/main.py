from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_string):
    # Implement a basic sanitization logic here
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_', '@', '#'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitize_input(host))
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}