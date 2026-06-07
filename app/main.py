from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        # Secure implementation
        subprocess.run(['ping', '-c 1', host], check=True, shell=False)
        return {"status": "completed"}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {"error": str(e)}