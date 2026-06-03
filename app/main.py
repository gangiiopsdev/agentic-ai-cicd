from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        raise Exception(f"Ping failed with error: {e.stderr.decode('utf-8')}"