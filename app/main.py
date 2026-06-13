from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> str:
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        return host
    else:
        raise ValueError("Invalid host")

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        subprocess.run(['ping', sanitized_host], check=True, shell=False)  # Use subprocess.run with check=True for better error handling
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}
    except subprocess.CalledProcessError as e:
        return {"error": f"Ping failed: {e}"}