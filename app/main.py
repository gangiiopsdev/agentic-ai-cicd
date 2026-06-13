from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    if validate_host(host):
        result = await subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts