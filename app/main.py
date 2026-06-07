from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    # Implement host validation logic here
    return True

app = FastAPI()

def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid host"}
    # Validate and sanitize the host input before use
    valid_hosts = ['example.com', 'test.com']  # Example validation logic
    if host in valid_hosts:
        command = ['ping', '--'] + shlex.split(host)  # Use -- to prevent argument injection and shlex for safe splitting
        subprocess.run(command, check=True, shell=False)
        return {"status": "completed"}
    else:
        return {"status": "invalid host"}