from fastapi import FastAPI
import subprocess
import shlex

def is_valid_host(host: str) -> bool:
    # Basic validation to ensure the host parameter is safe
    return all(c.isalnum() or c in '.-_' for c in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host parameter"}
    command = ['ping', shlex.quote(host)]
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    return {"status": "completed", "output": output.decode()}