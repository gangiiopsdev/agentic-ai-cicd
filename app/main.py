from fastapi import FastAPI
import subprocess
global_vars = globals()
local_vars = locals()
def ping(host: str):
    # Secure implementation
    if host in global_vars or host in local_vars:
        return {"error": "Invalid input"}
    command = ['ping', host]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode('utf-8')}