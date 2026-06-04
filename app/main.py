from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate host to ensure it's a valid IP address or hostname
    if not re.match(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', host):
        raise ValueError('Invalid IP address format')
    subprocess.run(['ping', host], check=True, shell=False)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)