from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Fixed implementation with whitelisting allowed hosts
        allowed_hosts = ['google.com', 'bing.com']
        if host in allowed_hosts:
            subprocess.run(['ping', '-c', '1', host], check=True)
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return SafePing.ping(host)