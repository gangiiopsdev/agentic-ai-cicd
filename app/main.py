from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    return host.replace('.', '').replace('-', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {
            "status": "failed",
            "error": "Invalid host"
        }
    try:
        output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {
            "status": "completed",
            "output": output.decode()
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": e.output.decode()
        }