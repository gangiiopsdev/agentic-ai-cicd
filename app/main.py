from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        # Validate and sanitize the host input
        if not is_valid_host(host):
            raise ValueError("Invalid host")
        output = subprocess.check_output(shlex.split(f'ping {host}'), timeout=5, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output)

# Helper function to validate the host input
def is_valid_host(host):
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

@app.get("/ping")
def ping(host: str):
    # Using a safe function to handle the ping command
    result = safe_ping(host)
    return {"status": "completed", "result": result}