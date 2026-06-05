from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'stdout': result.stdout.decode('utf-8'), 'stderr': result.stderr.decode('utf-8')}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)