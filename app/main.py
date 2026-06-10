from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host):
    # Safe implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)