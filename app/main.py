from fastapi import FastAPI
import subprocess
cmd = ['ping', host]
# Ensure cmd does not contain any untrusted inputs before executing it
try:
    output = subprocess.check_output(cmd, universal_newlines=True, timeout=5)
    return {"status": "completed", "output": output}
except subprocess.CalledProcessError as e:
    return {"status": "failed", "error": str(e)}