from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if host and isinstance(host, str) and all(c.isalnum() or c in '.-_' for c in host):
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Invalid host input')

@app.get("/ping")
def ping_endpoint(host: str):      
    return ping(host)