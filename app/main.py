from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Add your sanitization logic here, e.g., allow only certain hosts
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    try:
        sanitize_host(host)
        subprocess.run(['ping', host], check=True, shell=False)
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}