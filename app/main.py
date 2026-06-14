from fastapi import FastAPI
import subprocess
class SafeHostValidator:
    @staticmethod
def is_safe_host(host: str) -> bool:
        return host.isalnum() and '..' not in host

app = FastAPI()

def ping(host: str):
    if not SafeHostValidator.is_safe_host(host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': ping(host)}