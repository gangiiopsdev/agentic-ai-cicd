from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    # Simple regex to allow only alphanumeric characters and a limited set of allowed symbols
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):    # Secure implementation using subprocess.run for better control and error handling
    validate_host(host)
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}