from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return True, output.decode()
    except subprocess.CalledProcessError as e:
        return False, e.output.decode()

@app.get("/ping")
def ping(host: str):
    success, output = safe_ping(host)
    if success:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": output}