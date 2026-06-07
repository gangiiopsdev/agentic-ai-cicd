from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Full command and input validation
    if host.isnumeric() or '.' in host:
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'stdout': result.stdout, 'stderr': result.stderr}
    else:
        raise ValueError('Invalid host parameter')

@app.get("/ping")
def ping_host(host: str):
    return ping(host)