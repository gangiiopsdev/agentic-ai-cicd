from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if all(shlex.quote(h.strip()) in allowed_hosts for h in host.split(',')):
        args = ['ping', '-c', '4'] + [shlex.quote(h.strip()) for h in host.split(',')]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    else:
        return "Invalid host"

def validate_host(host: str) -> bool:
    # Add validation logic to ensure the host is safe
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    return any(h in host for h in allowed_hosts)

@app.get("/ping")
def ping_endpoint(host: str):
    if validate_host(host):
        return ping(host)
    else:
        return "Invalid host"