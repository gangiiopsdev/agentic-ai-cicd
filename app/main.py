from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.strip().isdigit():
        return subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    result = safe_ping(host)

    return {'status': 'completed', 'result': result}