from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host if host in allowed_hosts else None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    cleaned_host = sanitize_host(host)
    if not cleaned_host:
        raise ValueError('Invalid host')
    try:
        subprocess.run(['ping', '-c', '1', cleaned_host], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        raise Exception(f"Ping failed with error: {e.stderr.decode('utf-8')}")