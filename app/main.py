from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        raise Exception(f"Ping failed with error: {e.stderr.decode('utf-8')}")