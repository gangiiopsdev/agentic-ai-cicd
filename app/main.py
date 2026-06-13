from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host or ' ' in host:
        raise ValueError('Invalid host input')
    return subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'error': str(e)}, 400