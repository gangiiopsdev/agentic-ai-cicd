from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add your validation logic here, e.g., allow only certain domains or IP addresses
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {"status": "completed", "output": output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output.decode('utf-8')}
    else:
        return {"status": "failed", "error": "Invalid host"}