from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not subprocess.call(['ping', '-c', '1', host]):
        return {"status": "completed"}
    else:
        raise Exception("Ping failed")