from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        try:
            output = subprocess.check_output(shlex.split('ping ' + host), stderr=subprocess.STDOUT, timeout=5)
            return {"status": "completed", "output": output.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
        except subprocess.TimeoutExpired:
            return {"status": "timeout"}
    else:
        return {"status": "failed", "error": "Invalid host"}