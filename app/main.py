from fastapi import FastAPI
import subprocess

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
    # Basic validation to prevent injection attacks
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    return host in allowed_hosts