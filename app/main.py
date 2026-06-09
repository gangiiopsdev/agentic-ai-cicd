from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add validation logic here to ensure host is safe
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        # Secure implementation using list instead of shell=True
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {'error': 'Invalid host'}, 400