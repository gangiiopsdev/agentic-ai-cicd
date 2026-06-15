from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.run and shlex.quote
    from shlex import quote
    command = ["ping", quote(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}