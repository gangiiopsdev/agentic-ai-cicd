from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        allowed_hosts = ['127.0.0.1', '::1']
        if host not in allowed_hosts:
            raise ValueError('Invalid host')
        subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafeSubprocess.ping(host)