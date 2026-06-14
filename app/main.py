from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Add more hosts as needed
    if host not in allowed_hosts:
        raise ValueError(f'Invalid host: {host}')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}