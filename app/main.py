from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        args = shlex.split(f'ping -c 1 {shlex.quote(host)}')
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get("/ping")
def ping(host: str):
    success, output = safe_ping(host)
    if not success:
        return {"status": "failed", "message": "Invalid host", "output": output}
    return {"status": "completed", "output": output}