from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return shlex.quote(input_string)

def validate_host(host: str):
    allowed_hosts = ['example.com', 'another-example.com']  # Add a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        sanitized_host = sanitize_input(host)
        output = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}