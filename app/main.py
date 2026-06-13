from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        subprocess.run(["ping", host], check=True, capture_output=True, text=True)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}