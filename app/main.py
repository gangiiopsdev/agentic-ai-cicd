from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    escaped_host = shlex.quote(host)
    subprocess.call(['ping', escaped_host])

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.quote to escape shell injection
    safe_ping(host)
    return {'status': 'completed'}