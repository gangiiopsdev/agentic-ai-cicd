from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    stdout, stderr = safe_ping(host)
    return {'status': 'completed', 'stdout': stdout, 'stderr': stderr}