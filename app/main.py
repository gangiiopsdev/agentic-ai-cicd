from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    return all(c.isalnum() or c in ['-', '.', '_'] for c in hostname)

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {"status": "failed", "error": "Invalid hostname"}
    args = ['ping', host]
    try:
        subprocess.check_output(args, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    return {"status": "completed"}