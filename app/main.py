from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    if host in allowed_hosts:
        return True
    return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):,
    # Validate and sanitize the host input
    if not safe_ping(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.run(shlex.split('ping ' + shlex.quote(host)), capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}