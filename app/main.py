from fastapi import FastAPI
import subprocess
global allowed_hosts
allowed_hosts = ['8.8.8.8', '127.0.0.1']

app = FastAPI()
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        result = safe_ping(host)
        return {"status": "completed", "result": result}
    else:
        return {"status": "error", "message": "Invalid host provided"}
def validate_host(host: str) -> bool:
    global allowed_hosts
    # Enhanced validation to prevent injection attacks
    import re
    pattern = re.compile(r'^\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b$')
    return bool(pattern.match(host))