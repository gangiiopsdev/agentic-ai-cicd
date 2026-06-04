from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add validation logic here, e.g., allow only specific IP addresses or domains
    allowed_hosts = ['example.com', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}