from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', '-c', '1', f'{host}'], check=True, shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}