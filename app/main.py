from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize host input
    if not all(c.isalnum() or c in '-._' for c in host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'stdout': result.stdout, 'stderr': result.stderr}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)