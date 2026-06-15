from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if validate_host(host):
        command = ['ping', shlex.quote(host)]
        subprocess.run(command, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

# Add a function to validate the host input
def validate_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts