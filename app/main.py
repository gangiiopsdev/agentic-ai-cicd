from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        try:
            cmd = ['ping', host]
            output = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "output": output.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr.decode()}
    else:
        return {"status": "failed", "error": "Host not allowed"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)