from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    # Implement validation logic here
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = shlex.split(f'ping {host}')
    result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode()}