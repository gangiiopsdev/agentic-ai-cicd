from fastapi import FastAPI
import subprocess
import shlex
class CommandExecutionException(Exception):
    pass

app = FastAPI()

def secure_ping(host):
    # Ensure host input is safe and validated
    if not validate_host(host):
        raise ValueError("Invalid host")
    command = ['ping', host]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise CommandExecutionException(e.stderr)

@app.get="/ping"
def ping(host: str):
    return secure_ping(host)

def validate_host(host):
    # Implement validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts