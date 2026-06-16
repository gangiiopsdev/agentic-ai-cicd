from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Add logic to validate and sanitize host input here
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        sanitize_host(host)
        # Use check_output to avoid shell=True and improve security
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {"status": "completed", "result": "Success"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}