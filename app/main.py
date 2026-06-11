from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = shlex.split(f'ping {host}')
    try:
        output = subprocess.check_output(args, universal_newlines=True, timeout=5)
        return True, output
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get("/ping")
def ping(host: str):
    success, result = safe_ping(host)
    if success:
        return {"status": "completed", "output": result}
    else:
        return {"status": "failed", "error": result}