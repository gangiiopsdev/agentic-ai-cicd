from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    return host in allowed_hosts
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        try:
            result = subprocess.run(shlex.split(f'ping {host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "reason": str(e)}
    else:
        return {"status": "failed", "reason": "Invalid host"}