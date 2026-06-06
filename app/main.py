from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def is_valid_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid input"}

    try:
        result = subprocess.run([shlex.quote('ping'), shlex.quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}