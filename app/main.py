from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        command = ['ping', '--'] + [host]  # Use -- to prevent argument injection
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}