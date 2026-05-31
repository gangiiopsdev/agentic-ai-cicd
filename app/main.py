from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate host input before using it in subprocess
    if validate_host(host):
        command = ['ping'] + shlex.split(host)
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid or unsafe host')

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

# Define a function to validate the host input
def validate_host(host: str) -> bool:
    # Add validation logic here (e.g., whitelist of allowed hosts)
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts