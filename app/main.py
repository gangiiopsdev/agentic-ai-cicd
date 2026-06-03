from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Sanitize input to avoid command injection
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', subprocess.check_output(['echo', host]).decode().strip()]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)