from fastapi import FastAPI
import subprocess
from shlex import quote

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['.', '-', '_'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with full path and shell=False
    sanitized_host = subprocess.run(["/bin/ping", quote(sanitize_input(host))], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": sanitized_host.stdout}