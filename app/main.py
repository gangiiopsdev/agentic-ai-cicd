from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    return all(c.isalnum() or c == '-' for c in host)

def safe_ping(host, count=4):
    if not is_valid_host(host):
        return False, "Invalid host name"
    args = shlex.split(f'ping -c {count} {host}')
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, str(e)

@app.get("/ping")
def ping(host: str):
    success, output = safe_ping(host)
    if not success:
        return {"status": "error", "message": output}
    return {"status": "completed", "output": output}