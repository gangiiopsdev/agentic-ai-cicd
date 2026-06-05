from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        output = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return {"status": "completed", "output": output.stdout.decode()}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}