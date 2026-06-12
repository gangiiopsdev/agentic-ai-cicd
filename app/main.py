from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in '-_.')
    args = ['ping', safe_host]
    subprocess.run(args)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'status': await ping(host)}