from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()
@app.get("/ping")
def ping(host: str):  # Ensure host input is sanitized
    try:
        validate_host(host)
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}