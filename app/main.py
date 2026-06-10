from fastapi import FastAPI
import subprocess
import shlex
class HostValidator:
    @staticmethod
def is_valid_host(host):
        return host.replace('.', '').replace('-', '').isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validator = HostValidator()
    if not validator.is_valid_host(host):
        return {
            "status": "failed",
            "error": "Invalid host"
        }
    try:
        output = subprocess.check_output(['ping', '-c 1', host], stderr=subprocess.STDOUT, timeout=5)
        return {
            "status": "completed",
            "output": output.decode()
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": e.output.decode()
        }