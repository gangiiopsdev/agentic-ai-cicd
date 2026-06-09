from fastapi import FastAPI
import subprocess
cmd = ['ping', host]
# Safe implementation
try:
    output = subprocess.check_output(cmd, universal_newlines=True, timeout=5)
    return {"status": "completed", "output": output}
except Exception as e:
    return {"status": "failed", "error": str(e)}