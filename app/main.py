from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        subprocess.run(['ping', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping_handler(host: str):
    result = ping(host)
    return {"status": "completed", "result": result}