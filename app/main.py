from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use shlex to safely split the command line
        args = shlex.split('ping ' + host)
        result = subprocess.run(args, capture_output=True, text=True, timeout=5, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
    except Exception as e:
        return str(e)

def validate_host(host: str):
    # Add validation logic here to ensure the host is safe
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    return {"status": safe_ping(host)}