from fastapi import FastAPI
import subprocess

def is_valid_host(host: str) -> bool:
    # Simple example of host validation
    return '.' in host and len(host.split('.')) == 4

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host provided')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'stdout': result.stdout.strip(), 'stderr': result.stderr.strip()}

# Preventive controls:
# 1. Use a whitelist of allowed hosts.
# 2. Sanitize input to remove any special characters or escape sequences.