from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host parameter"}
    command = ['ping', host]
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    return {"status": "completed", "output": output.decode()}

def is_valid_host(host: str) -> bool:
    # Basic validation to ensure the host parameter is safe
    return all(c.isalnum() or c in '.-_' for c in host)