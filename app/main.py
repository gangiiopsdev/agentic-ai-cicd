from fastapi import FastAPI
import subprocess
import shlex

def run_ping(host):
    # Use subprocess.run instead of subprocess.call and avoid using shell=True
    try:
        result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

global_vars = globals()
local_vars = locals()
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Call the function securely
    if host in global_vars or host in local_vars:
        raise ValueError('Host cannot be a global or local variable name')
    return run_ping(shlex.quote(host))