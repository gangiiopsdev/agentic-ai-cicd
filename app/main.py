from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isnumeric():
        return False
    return True

@app.get="/ping")
def ping(host: str):
    if safe_ping(host):
        result = subprocess.call(['ping', '-c', '1', host])
        return {'status': 'completed', 'result': result}
    else:
        return {'error': 'Invalid host'}, 400