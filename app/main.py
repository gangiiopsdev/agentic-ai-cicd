from fastapi import FastAPI
import subprocess
from shlex import quote
generate_subprocess = lambda args: subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not all(c.isalnum() or c in ('-', '.', '_', ':', '/') for c in host):
        raise ValueError('Invalid host name')
    args = ['ping', quote(host)]
    result = generate_subprocess(args)
    return {"status": "completed", "output": result.stdout, "error": result.stderr}