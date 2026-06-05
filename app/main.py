from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Simple check for localhost
    return host in ['127.0.0.1', '::1', 'localhost']

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}