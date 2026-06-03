from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(shlex.split(' '.join(args)), capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    else:
        return {"status": "invalid host", "error": "Host not allowed"}

def validate_host(host):
    # Add validation logic here, e.g., regex to allow only specific domains/IPs
    import re
    pattern = r'^([0-9]{1,3}\.[0-9]{1,3}\.){2}[0-9]{1,3}$'  # Example for IP address validation
    return bool(re.match(pattern, host))