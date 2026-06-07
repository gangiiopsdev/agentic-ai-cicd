from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host:
        return False
    # Safe implementation using check_output with proper argument handling
    try:
        result = subprocess.check_output(['ping'] + shlex.split(host), stderr=subprocess.STDOUT, timeout=5)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.output.decode()}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}