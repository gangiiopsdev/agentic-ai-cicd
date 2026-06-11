from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        return False
    return True

def ping(host: str):
    if validate_host(host):
        try:
            output = subprocess.check_output(['ping', host], shell=False, universal_newlines=True, timeout=5)
            return {"status": "completed", "output": output}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Invalid host"}