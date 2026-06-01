from fastapi import FastAPI
import subprocess
cimport = subprocess.CalledProcessError
cmd = ['ping', host]
if not host.isalnum() and not '.' in host:
    raise ValueError("Invalid host format")
try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
except cim as e:
    return {"status": "failed", "output": str(e)}
return {"status": "completed", "output": result.stdout}