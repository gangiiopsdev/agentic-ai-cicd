from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Define a list of allowed hosts or patterns
    allowed_hosts = ['example.com', 'test.example.com']
    if host in allowed_hosts:
        try:
            cmd = ['ping'] + shlex.split(host)
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=10)
            return {"status": "completed", "output": output.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": e.output.decode()}
    else:
        return {"status": "error", "message": "Invalid host"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)