from fastapi import FastAPI
import subprocess
globally_allowed_hosts = {'example.com', 'test.com'}

app = FastAPI()

def ping(host: str):
    if host in globally_allowed_hosts:
        # Secure implementation with whitelist
        subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)