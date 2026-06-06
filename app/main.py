from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    return subprocess.call(args)

@app.get="/ping")
def ping(host: str):
    # Safe implementation
    result = safe_ping(host)
    if result == 0:
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'code': result}