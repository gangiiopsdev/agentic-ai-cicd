from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"error": "Invalid host"}
    return {"status": safe_ping(host)}

def is_safe_host(host: str) -> bool:
    # Add logic to validate the host input, e.g., allow only specific domains or IP addresses
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts