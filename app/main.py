from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)