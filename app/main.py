from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

def validate_host(host: str):
    if not all(c.isalnum() or c.isspace() for c in host):
        raise ValueError('Invalid host input')
    return host

def execute_command(command: list):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return None

@app.get("/ping")
def ping(host: str = validator(validate_host)):  # Validate host input here
    sanitized_host = shlex.quote(host)
    command = ['ping', sanitized_host]
    output = execute_command(command)
    if output is not None:
        return {"status": "completed", "output": output}
    else:
        return {"status": "error", "error_message": str(e)}