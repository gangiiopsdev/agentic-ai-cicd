from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation for host format
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.stderr.decode())}