from fastapi import FastAPI
import subprocess
host = 'example.com'  # Replace with actual host input validation
if isinstance(host, str) and all(c.isalnum() or c in ('.', '-', '_') for c in host):
    cmd = ['ping', host]
    try:
        output = subprocess.check_output(cmd, universal_newlines=True, timeout=5)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
else:
    return {"status": "failed", "error": "Invalid host input"}