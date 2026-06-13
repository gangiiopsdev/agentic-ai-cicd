from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_ping(host: str):
    if valid_host(host):
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"error": str(e)}
def valid_host(host: str) -> bool:
    # Simple validation, replace with actual validation logic
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts