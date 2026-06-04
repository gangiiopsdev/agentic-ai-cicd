from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        args = ["ping", host]  # Use list instead of shell=True and f-string
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return True, output.decode()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return False, str(e.output.decode())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    is_valid, result = safe_ping(host)
    if is_valid:
        return {"status": "completed", "output": result}
    else:
        return {"status": "failed", "error": result}