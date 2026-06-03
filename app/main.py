from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use a whitelist of allowed hosts
        if host not in ['allowed_host1', 'allowed_host2']:
            raise ValueError('Invalid host')
        output = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return safe_ping(host)
    else:
        return 'Invalid host'

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., whitelist specific hosts
    return True