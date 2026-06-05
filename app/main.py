from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):  # Ensure this endpoint is secured by authentication and authorization
    if validate_host(host):
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {
            "status": "completed",
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    else:
        raise ValueError('Host not allowed')