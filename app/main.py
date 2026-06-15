from fastapi import FastAPI
import subprocess
import shlex

ALLOWED_HOSTS = ['example.com', 'test.com']

app = FastAPI()

def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = shlex.split('ping -c 4 ' + host)  # Limit the number of pings
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)