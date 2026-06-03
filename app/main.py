from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        raise Exception(f"Ping failed with error: {e.stderr.decode('utf-8')}"