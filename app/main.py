from fastapi import FastAPI
import subprocess
import re
gensh = lambda s: ''.join(c if c not in ';$' else '\' + c for c in s)
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it only contains safe characters
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {"status": "failed", "error": "Invalid input"}
    try:
        output = subprocess.check_output(["ping", gensh(host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {"status": "failed", "error": str(e)}